certbot-dns-hcloud
==================

`Hetzner Cloud`_ DNS Authenticator plugin for Certbot

This plugin automates the process of completing a ``dns-01`` challenge by
creating, and subsequently removing, TXT records using the Hetzner Console API.

.. _Hetzner Cloud: https://console.hetzner.com/projects/
.. _certbot: https://certbot.eff.org/

Installation
------------

::

    pip install git+https://github.com/EMX107/certbot-dns-hcloud


Named Arguments
---------------

To start using DNS authentication for HCloud, pass the following arguments on
certbot's command line:

==================================== ==============================================
``--authenticator dns-hcloud``       select the authenticator plugin (Required)

``--dns-hcloud-credentials``         ispconfig Remote User credentials
                                     INI file. (Required)

``--dns-hcloud-propagation-seconds`` | waiting time for DNS to propagate before asking
                                     | the ACME server to verify the DNS record.
                                     | (Default: 60, Recommended: >= 120)
==================================== ==============================================


Credentials
-----------

An example ``credentials.ini`` file:

.. code-block:: ini

   dns_hcloud_api_token = j8foaU8u2irpupAHwaf...

The path to this file can be provided interactively or using the
``--dns-hcloud-credentials`` command-line argument. Certbot
records the path to this file for use during renewal, but does not store the
file's contents.

**CAUTION:** You should protect these API credentials as you would the
password to your ispconfig account. Users who can read this file can use these
credentials to issue arbitrary API calls on your behalf. Users who can cause
Certbot to run using these credentials can complete a ``dns-01`` challenge to
acquire new certificates or revoke existing certificates for associated
domains, even if those domains aren't being managed by this server.

Certbot will emit a warning if it detects that the credentials file can be
accessed by other users on your system. The warning reads "Unsafe permissions
on credentials configuration file", followed by the path to the credentials
file. This warning will be emitted each time Certbot uses the credentials file,
including for renewal, and cannot be silenced except by addressing the issue
(e.g., by using a command like ``chmod 600`` to restrict access to the file).


Examples
--------

To acquire a single certificate for both ``example.com`` and
``*.example.com``, waiting 900 seconds for DNS propagation:

.. code-block:: bash

   certbot certonly \
     --authenticator dns-hcloud \
     --dns-hcloud-credentials /etc/letsencrypt/.secrets/hetzner/certbot.ini \
     --dns-hcloud-propagation-seconds 900 \
     -d 'example.com' \
     -d '*.example.com'


Docker
------

In order to create a docker container with a certbot-dns-ispconfig installation,
create an empty directory with the following ``Dockerfile``:

.. code-block:: docker

    FROM certbot/certbot
    RUN pip install git+https://github.com/EMX107/certbot-dns-hcloud

Proceed to build the image::

    docker build -t certbot/dns-hcloud .

Once that's finished, the application can be run as follows::

    docker run --rm \
       -v /var/lib/letsencrypt:/var/lib/letsencrypt \
       -v /etc/letsencrypt:/etc/letsencrypt \
       --cap-drop=all \
       certbot/dns-hcloud certonly \
       --authenticator dns-hcloud \
       --dns-hcloud-propagation-seconds 900 \
       --dns-hcloud-credentials \
           /etc/letsencrypt/.secrets/domain.tld.ini \
       --no-self-upgrade \
       --keep-until-expiring --non-interactive --expand \
       -d example.com -d '*.example.com'

It is suggested to secure the folder as follows::
chown root:root /etc/letsencrypt/.secrets
chmod 600 /etc/letsencrypt/.secrets