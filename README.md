# web-browser-parser

## 기능
chrome history의 urls, keyword_search_terms, downloads </br>
edge history의 urls, keyword_search_terms, downloads </br>
firefox places.sqlite의 moz_places, moz_bookmarks, moz_annos </br>

C:/Users/username/Desktop/forensic_artifact 위치로 csv로 추출(forensic_artifact폴더 자동 생성)

## Command Line Interface

```
options:
  -h, --help  show this help message and exit
  --c         chrome artifact
  --e         edge artifact
  --f         firefox artifacts
  --a         All Artifacts

Examples : python wbparser.py --h 
           python wbparser.py --a
  
