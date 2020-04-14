[atlas-repo]: https://github.com/shadow/atlas

The code to generate a shadow network topology is [here][atlas-repo] and has
its own READMEs. What follows is some information regarding the input data
specifically.

For the latency portion, [here][2018-ripepairs] is the final output of our RIPE
measurements and data parsing process from 2018. We did not rerun this
collection process in 2020.

For the bandwidth portion, we provide here archives www.speedtest.net as it
appeared in [2018][2018-speedtest] and [2020][2020-speedtest]. Here are the
final JSON output files of the parsing process in [2018][2018-speeddata] and
[2020][2020-speeddata].

[2018-ripepairs]: data/shadow/network/latency/2018-all-pairs.csv.xz

[2018-speedtest]: data/shadow/network/bandwidth/2018-www.speedtest.net.txz
[2020-speedtest]: data/shadow/network/bandwidth/2020.04-www.speedtest.net.txz

[2018-speeddata]: data/shadow/network/bandwidth/2018-speed-data.json.xz
[2020-speeddata]: data/shadow/network/bandwidth/2020.04-speed-data.json.xz

If you want to reproduce our results with fresh data, you will need

1. a MaxMind account to download their GeoIP databases for both the latency and
   bandwidth parts of topology generation.
1. to scrape part www.speedtest.net for the bandwidth part.

# GeoIP data

MaxMind does not allow us to provide the databases that we used. What follows
is information on how to download the (current) databases for yourself.

Create a MaxMind account [here](https://www.maxmind.com/en/geolite2/signup).

After logging in, visit your *Account Summary* page.

You can now download GeoLite2 databases in two ways: in the browser manually,
or via a URL with your license key for scripting.

In the links that follow, you will have to edit the ones with place-holder
account number `222222` in them.

## Manual with browser

Visit the *Download Files* page
<https://www.maxmind.com/en/accounts/222222/geoip/downloads>.

Click on the *Download GZIP* link for *GeoLite2 City*. It should download a
`.tar.gz`.

Click on the *Download ZIP* link for *GeoLite2 City: CSV Format*. It should
download a `.zip`.

## License key for scripting

Visit the *My License Key* page
<https://www.maxmind.com/en/accounts/222222/license-key>. Generate a new
license key. No it won't be used for GeoIP Update. The next page will show you
your account number and license key. Take note of it. It will look something
like `nNnNnNnNnNnNnNnN`.

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

# Speed test data

Verify that <https://www.speedtest.net/reports/> still lists reports for a
variety of countries and clicking on the links for countries leads to pages
with per-city data in tables.

Verify that <https://www.speedtest.net/global-index> still lists averages for a
wide variety of countries.

The [code repo][atlas-repo] walks you through how to download and parse this
data.

# Caveats

Do not expect the data from 2018 to work with scripts in the [code
repo][atlas-repo] without some sort of modification: the scripts were
organized, documented, and updated in 2020, but the 2018 data is merely
provided as-is.

We expect the main pain points with processing 2018 data today to be:

- revision of scripts in 2020 added city names to latency data output, but 2018
  didn't include those.
- 2018 bandwidth data parsing was even more of a manual process than in 2020,
  so there isn't really an intermediate representation of the data.
