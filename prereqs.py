# Run this first to install pre reqs

import pip


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])




depens = [
        'yt-dlp',
        'requests',
        'google-api-python-client',
        'google-auth-oauthlib',
        'json',
        'time',
        'flask'
        ]

# Example
if __name__ == '__main__':
    for package in depens:
        install(package)
