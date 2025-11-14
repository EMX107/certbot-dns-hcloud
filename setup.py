from setuptools import setup

install_requires = [
    'hcloud>=2.11.0',
    'certbot>=5.1.0',
    'setuptools'
]

setup(
    name='certbot-dns-hcloud',
    version='1.0.3',
    author='EMX107',
    license='Apache License 2.0',
    url='https://github.com/EMX107/certbot-dns-hcloud',
    python_requires='>=3.13',
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-hcloud = certbot_dns_hcloud.dns_hcloud:Authenticator'
        ]
    },
)