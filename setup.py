from setuptools import setup, find_packages

install_requires = [
    'hcloud>=2.11.0',
    'certbot>=5.1.0',
    'setuptools'
]

with open('README.rst', 'r') as f:
    description = f.read()

setup(
    name='certbot-dns-hcloud',
    version='1.1.1',
    author='EMX107',
    license='Apache License 2.0',
    long_description=description,
    long_description_content_type='text/x-rst',
    url='https://github.com/EMX107/certbot-dns-hcloud',
    python_requires='>=3.13',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-hcloud = certbot_dns_hcloud.dns_hcloud:Authenticator'
        ]
    },
)