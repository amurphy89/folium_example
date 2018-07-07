from setuptools import setup

def readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(name='Folium Map Example',
    version='0.1',
    author='Ash Murphy',
    author_email='amurphy9956@live.com',
    description='A working example of Folium',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Topic :: Geo Mapping :: Analytics',
    ],
    keywords='folium pandas geography analytics',
    packages=['folium_map'],
    scripts=['bin/folium-map'],
    install_requires=[
        'folium',
        'markdown',
        'pandas',
        'pytest',
    ],
    include_package_data=True,
    zip_safe=False)
