
## 概要
「アトランチスの謎」のワープ構成を可視化

## ファイル構成
```mermaid
graph LR
	scrape_and_dump[scrape_and_dump.py] -- 出力 --> json[atlantis.json]
	find_deadend[find_deadend.py] -- 読み込み --> json
	find_far_route[find_far_route.py] ---> find_route
	find_missing_zone[find_missing_zone.py] ---> find_route
	find_route[find_route.py] -- 読み込み --> json
	find_route_all[find_route_all.py] ---> find_route
	find_route_to[find_route_to.py] ---> find_route
	scrape_and_dump -- 参照 --> net[ネット情報]
	find_route_to -- 出力 --> md[atlantis.md]
	find_route_all -- 出力 --> md[atlantis.md]

	subgraph Python
	scrape_and_dump
	find_deadend
	find_far_route
	find_missing_zone
	find_route
	find_route_all
	find_route_to
	scrape_and_dump
	find_route_to
	find_route_all
	end
```

## 使い方
1. ネット情報を読み込みJSONファイル化
```
python3 scrape_and_dump.py
```
2. 可視化
2.1 行き止まりを検出
```
python3 find_deadend.py
```
2.2 最もワープを要するゾーンを探索
```
python3 find_far_route.py
```
2.3 到達できないゾーンを検出
```
python3 find_missing_zone.py
```
2.4 全ゾーンのつながりを可視化
```
python3 find_route_all.py
```
2.5 指定のゾーンへのつながりを可視化
```
python3 find_route_all.py zone limit
```
