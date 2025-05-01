# TrendTags - Tag Generator 

[![CI Status](https://github.com/imDarshanGK/TrendTags/actions/workflows/main.yml/badge.svg)](https://github.com/imDarshanGK/TrendTags/actions)
[![CodeQL](https://github.com/imDarshanGK/TrendTags/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/imDarshanGK/TrendTags/actions)

## Features 

- Real-time tag generation from YouTube trends
- One-click copy all tags
- Clean responsive interface
- Fast Flask-powered backend
- Auto-updating tag database

## Installation 🛠️

### Prerequisites
- Python 3.8+
- YouTube API key

### Quick Start
```bash
git clone https://github.com/your-username/TrendTags.git
cd TrendTags

# Set up environment
pip install -r requirements.txt
```

Create a `.env` file in the root directory of the project and add your API keys.  
You can use the provided `.env.example` as a reference.

Then edit `.env` and replace placeholder values:

```env
YOUTUBE_API_KEY=your_actual_youtube_api_key
RAPIDAPI_KEY=your_actual_rapidapi_key
```

```bash
# Run the application
python app.py
```

## Usage
1. Enter your video topic (e.g., "cooking", "tech reviews")
2. Select number of tags (10-30)
3. Click "Generate Tags"
4. Copy tags with one click

## Project Structure 
```bash

TrendTags/
├── .github/           # CI/CD workflows
│   ├── workflows/     # GitHub Actions
│   └── codeql/        # Security config
├── static/            # Frontend assets
│   ├── css/           # Stylesheets
│   └── js/            # JavaScript
├── templates/         # HTML templates
├── app.py             # Main application
├── config.py          # Configuration
├── requirements.txt   # Dependencies
├── LICENSE            # MIT License
└── README.md          # This file
```

## Contributing
We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for:

* How to report issues
* Code style guidelines
* Pull request process
* Commit message standards


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

