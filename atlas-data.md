[atlas-repo]: https://github.com/shadow/atlas

The code to generate a shadow network topology is [here][atlas-repo] and has
its own READMEs. What follows is some information regarding the input data
specifically.

You will need a MaxMindDB account to download their GeoIP databases for both
the latency and bandwidth parts of topolgoy generation. You will need to scrape
part www.speedtest.net for the bandwidth part too.

# GeoIP data

Create a MaxMind account [here](https://www.maxmind.com/en/geolite2/signup).

After logging in, visit your *Account Summary* page. You will have to edit
these links that have a place-holder account number `222222` in them.

Visit the My License Key page
<https://www.maxmind.com/en/accounts/222222/license-key>. Generate a new
license key. No it won't be used for GeoIP Update. The next page will show you
your account number and license key. Take note of it. It will look something
like `nNnNnNnNnNnNnNnN`.

You can now download GeoLite2 databases in two ways: in the browser manually,
or via a URL with your license key for scripting.

## Manual with browser

Visit the *Download Files* page
<https://www.maxmind.com/en/accounts/222222/geoip/downloads>.

Click on the *Download GZIP* link for *GeoLite2 City*. It should download a
`.tar.gz`.

Click on the *Download ZIP* link for *GeoLite2 City: CSV Format*. It should
download a `.zip`.

## Lincense key for scripting

You need the *GeoLite2 City* database and the *GeoLite2 City: CSV Format*
database. Replace `YOUR_LICENSE_KEY` in the following links to download
*GeoLite2 City*.

    # Database URL
    https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=YOUR_LICENSE_KEY&suffix=tar.gz
    # SHA256 URL
    https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=YOUR_LICENSE_KEY&suffix=tar.gz.sha256

And likewise with the following two links for *GeoLite2 City: CSV Format*.

    # Database URL
    https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City-CSV&license_key=YOUR_LICENSE_KEY&suffix=zip
    # SHA256 URL
    https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City-CSV&license_key=YOUR_LICENSE_KEY&suffix=zip.sha256
