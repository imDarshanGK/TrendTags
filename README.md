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

1. Clone the repository and navigate to it in the command line:
```bash
git clone https://github.com/your-username/TrendTags.git
cd TrendTags
```

2. Create `.env` file:
```bash
cp .env.example .env
nano .env  # Add your actual API keys
```

Then edit `.env` and replace placeholder values:

```env
# SECURITY WARNING!
# 1. Rename this to .env
# 2. Never commit real keys
# 3. Get keys from Google Cloud Console

YOUTUBE_API_KEY=your_key_here
RAPIDAPI_KEY=your_key_here
```

3. Set up environment:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
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