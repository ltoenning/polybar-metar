# polybar-metar

A script for polybar which displays METAR information of given airport by ICAO. It uses https://aviationweather.gov/ API as source.

## Dependencies
* Python3

## Configuration

Within polybar-metar.py you can change wheter the ICAO code is shown at the beginning of the line

## Module

```
[module/metar]
type = custom/script
interval = 1200
exec = python <PATH TO polybar-metar.py> <Airport ICAO>
```

**Example**

```
[module/metar]
type = custom/script
interval = 1200
exec = python /home/user/documents/polybar-metar.py EDDL
```

## Standalone usage
You can use this script also as standalone version for getting METAR information. It supports multiple ICAO codes seperated by `SPACE`.

**Example**

```
❯ python polybar-metar.py EDDL EDDK
EDDL 181120Z 12005KT 070V220 9999 FEW046 26/13 Q1019 NOSIG
EDDK 181120Z VRB05KT 9999 FEW043 25/14 Q1019 NOSIG
```
