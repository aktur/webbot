import platform
from setuptools import setup

install_requires = ['selenium']

with open('README.md' , 'r') as f:
    long_description = f.read() 

setup(
    name='webbot',
    packages = ['webbot','webbot.drivers'] ,
    version = '0.0.1',
    description = '' ,
    long_description = long_description , 
    summary = 'Offline Text to Speech library with multi-engine support'  ,
    author = 'Natesh M Bhat' ,
    url = 'https://github.com/nateshmbhat/pyttsx3',
    author_email = 'nateshmbhatofficial@gmail.com' ,
    #download_url = 'https://github.com/nateshmbhat/pyttsx3/archive/v2.6.tar.gz',
    keywords=['webbot', 'selenium' , 'autoweb','automate' , 'automation' ,'web' , 'autoweb' , 'auto' , 'pyauto', 'pyautogui'],
    classifiers = [] ,
)