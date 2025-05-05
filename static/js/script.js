document.addEventListener('DOMContentLoaded', function() {
    const topicInput = document.getElementById('topicInput');
    const searchBtn = document.getElementById('searchBtn');
    const maxResults = document.getElementById('maxResults');
    const tagsContainer = document.getElementById('tagsContainer');
    const sourceInfo = document.getElementById('sourceInfo');
    const copyBtn = document.getElementById('copyBtn');
    
    // Initialize with empty state
    initializeEmptyState();
    
    searchBtn.addEventListener('click', fetchTags);
    topicInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') fetchTags();
    });
    
    copyBtn.addEventListener('click', copyAllTags);
    
    function fetchTags() {
        const topic = topicInput.value.trim();
        const maxTags = maxResults.value;
        
        if (!topic) {
            showError('Please enter a topic');
            return;
        }
        
        // Show loading state
        showLoadingState();
        
        fetch('/get_tags', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `topic=${encodeURIComponent(topic)}&max_results=${maxTags}`
        })
        .then(handleResponse)
        .then(data => {
            if (data.error) {
                showError(data.error);
            } else {
                displayTags(data.tags, data.source);
            }
        })
        .catch(handleError);
    }
    
    function handleResponse(response) {
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    }
    
    function displayTags(tags, source) {
        tagsContainer.innerHTML = '';
        
        if (!tags || tags.length === 0) {
            showError('No tags found for this topic. Try a different search term.');
            return;
        }
        
        // Show source info
        sourceInfo.textContent = `Tags sourced from: ${source}`;
        
        // Display tags
        tags.forEach(tag => {
            createTagElement(tag);
        });
        
        // Show copy button
        copyBtn.classList.remove('hidden');
    }
    
    function createTagElement(tagText) {
        const tagElement = document.createElement('div');
        tagElement.className = 'tag';
        tagElement.textContent = tagText;
        tagElement.title = 'Click to copy';
        
        tagElement.addEventListener('click', function() {
            copyToClipboard(tagText);
            showCopiedFeedback(tagElement);
        });
        
        tagsContainer.appendChild(tagElement);
    }
    
    function copyAllTags() {
        const tags = Array.from(document.querySelectorAll('.tag'))
            .map(tag => tag.textContent)
            .join(', ');
        
        copyToClipboard(tags);
        showCopiedFeedback(copyBtn, '<i class="fas fa-check"></i> Copied!');
    }
    
    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).catch(err => {
            console.error('Could not copy text: ', err);
        });
    }
    
    function showCopiedFeedback(element, temporaryText = 'Copied!') {
        const originalText = element.innerHTML;
        element.innerHTML = temporaryText;
        
        setTimeout(() => {
            element.innerHTML = originalText;
        }, 1500);
    }
    
    function showLoadingState() {
        tagsContainer.innerHTML = '<div class="loading"></div>';
        sourceInfo.textContent = 'Loading...';
        copyBtn.classList.add('hidden');
    }
    
    function showError(message) {
        tagsContainer.innerHTML = `
            <div class="error-message">
                <i class="fas fa-exclamation-circle"></i> ${message}
            </div>
        `;
        sourceInfo.textContent = '';
        copyBtn.classList.add('hidden');
    }
    
    function handleError(error) {
        console.error('Error:', error);
        showError('Failed to load tags. Please try again later.');
    }
    
    function initializeEmptyState() {
        tagsContainer.innerHTML = `
            <div class="placeholder">
                <i class="fab fa-youtube"></i>
                <p>Enter a topic to generate YouTube tags</p>
            </div>
        `;
        sourceInfo.textContent = '';
        copyBtn.classList.add('hidden');
    }
});