from setuptools import setup


setup(
    name='heliotron',
    version='0.2.0',
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description='Simple library to interface with Philips Hue light bridges.',
    long_description=open('README.md').read(),
    license='MIT',
    keywords='philips hue rest api light',
    url='https://github.com/briancline/heliotron',
    packages=['heliotron'],
    install_requires=['astral'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Home Automation',
    ],
)
