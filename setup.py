# Always prefer setuptools over distutils
from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='TrollHunter',

    version='0.2.3',
    description='TrollHunter',
    url="https://github.com/StanGirard/TrollHunter",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPL",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
    ],

    packages=["TrollHunter.twitter_crawler","TrollHunter.twitter_crawler.twint_api",
              "TrollHunter.twitter_crawler.twint.twint","TrollHunter.twitter_crawler.twint.twint.storage",
              "TrollHunter.loggers","TrollHunter.news_crawler.sitemap","TrollHunter.news_crawler.database", "TrollHunter.texto", "TrollHunter.Gorafi"],

    install_requires=[
        "aiodns==2.0.0",
        "aiofiles==0.4.0",
        "aiohttp==3.6.2",
        "aiohttp-socks==0.3.4",
        "amqp==2.5.2",
        "aniso8601==8.0.0",
        "async-timeout==3.0.1",
        "attrs==19.3.0",
        "beautifulsoup4==4.8.2",
        "billiard==3.6.3.0",
        "blinker==1.4",
        "cchardet==2.1.5",
        "celery==4.4.1",
        "certifi==2019.11.28",
        "cffi==1.14.0",
        "chardet==3.0.4",
        "Click==7.0",
        "elasticsearch==7.5.1",
        "fake-useragent==0.1.11",
        "Flask==1.1.1",
        "Flask-Jsonpify==1.5.0",
        "Flask-RESTful==0.3.8",
        "Flask-SQLAlchemy==2.4.1",
        "geographiclib==1.50",
        "geopy==1.21.0",
        "googletransx==2.4.2",
        "h11==0.9.0",
        "h2==3.2.0",
        "hpack==3.0.0",
        "hyperframe==5.2.0",
        "idna==2.9",
        "influxdb==5.2.3",
        "importlib-metadata==1.5.0",
        "itsdangerous==1.1.0",
        "Jinja2==2.11.1",
        "kombu==4.6.8",
        "MarkupSafe==1.1.1",
        "multidict==4.7.5",
        "numpy==1.18.1",
        "pandas==1.0.1",
        "priority==1.3.0",
        "psycopg2-binary==2.8.4",
        "pycares==3.1.1",
        "pycparser==2.19",
        "PySocks==1.7.1",
        "python-dateutil==2.8.1",
        "pytz==2019.3",
        "requests==2.23.0",
        "schedule==0.6.0",
        "six==1.14.0",
        "soupsieve==2.0",
        "SQLAlchemy==1.3.13",
        "toml==0.10.0",
        "typing-extensions==3.7.4.1",
        "Unidecode==1.1.1",
        "urllib3==1.25.8",
        "vine==1.3.0",
        "Werkzeug==1.0.0",
        "wsproto==0.15.0",
        "yarl==1.4.2",
        "zipp==3.1.0",
        "nltk==3.4.5",
        "rake-nltk==1.0.4"
    ]

)

