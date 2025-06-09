# TrendTags - Tag Generator

[![Python Lint](https://github.com/imDarshanGK/TrendTags/actions/workflows/python-lint.yml/badge.svg)](https://github.com/imDarshanGK/TrendTags/actions)
[![CodeQL](https://github.com/imDarshanGK/TrendTags/actions/workflows/codeql.yml/badge.svg)](https://github.com/imDarshanGK/TrendTags/actions)

TrendTags is a real-time tag generator powered by YouTube trends, built with Flask and a clean, responsive frontend.

---

## Features

- 🔥 Real-time tag generation from YouTube trending videos
- 🪄 One-click “copy all tags” functionality
- 📱 Clean, responsive, and modern interface
- ⚡ Fast Flask-powered backend
- 🛡️ Auto-updating tag database
- 👨‍💻 Python linting, CodeQL security scanning via GitHub Actions

---

## Installation 🛠️

### Prerequisites

- Python >=3.12
- A YouTube API key (get one from Google Cloud Console)

### Quick Start

1. **Clone the repository and navigate to it:**
    ```bash
    git clone https://github.com/imDarshanGK/TrendTags.git
    cd TrendTags
    ```

2. **Create a `.env` file:**
    ```bash
    cp .env.example .env
    nano .env  # Add your actual API keys
    ```
    Edit `.env` and set your keys:
    ```env
    # SECURITY WARNING!
    # 1. Rename this to .env
    # 2. Never commit real keys
    # 3. Get keys from Google Cloud Console

    YOUTUBE_API_KEY=your_key_here
    RAPIDAPI_KEY=your_key_here
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

---

## Usage

1. Enter your video topic (e.g., "cooking", "tech reviews")
2. Select the number of tags (10–30)
3. Click "Generate Tags"
4. Copy tags with a single click

---

## Project Structure

```bash
TrendTags/
├── .github/           # CI/CD workflows
│   └── workflows/     # GitHub Actions
├── static/            # Frontend assets
│   ├── css/           # Stylesheets
│   └── js/            # JavaScript
├── templates/         # HTML templates
├── tests/             # Pytest tests
├── src/               # Source code
│   ├── config.py      # Configuration
│   └── ...            # Other modules
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT License
└── README.md          # This file
```

---

## Code Quality

Python code style and tests:
```bash
flake8 src tests app.py
black --check src tests app.py
pytest
```

---

## Security & Code Scanning

TrendTags uses [CodeQL](https://github.com/github/codeql-action) for code scanning via GitHub Actions.
You can view “Code scanning results” and security alerts in the [Security](../../security/code-scanning) tab of your repository.

---

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report issues
- Code style guidelines
- Pull request process
- Commit message standards

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.