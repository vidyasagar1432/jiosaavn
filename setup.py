from setuptools import setup
# from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = 'JioSaavn', 
    packages = ['JioSaavn'],
    version = 'v0.0.3',
    license='MIT', 
    description = 'Search for JioSaavn songs & album. Get song ,album & lyric information.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'vidya sagar', 
    author_email = 'svidya051@gmail.com',
    url = 'https://github.com/vidyasagar1432/JioSaavn',
    # download_url = '',
    keywords = ['jiosaavn', 'jiosaavnapi', 'songs', 'albums', 'lyrics'], 
    install_requires=[          
            'aiohttp',
        ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent', 
    'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)