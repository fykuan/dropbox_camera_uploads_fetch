dropbox_camera_uploads_fetch
============================

把Dropbox上的Camera Uploads資料夾下載並刪除

### 準備

1. 到 [https://www.dropbox.com/developers/core/sdks/python](https://www.dropbox.com/developers/core/sdks/python)下載 Dropbox Python SDK

2. 解壓縮並安裝
	
	python setup.py install

3. 到 [https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps) 選「Create APP Key」
4. 選擇「Dropbox API app」
5. 選擇「Files and datastores」
6. 選擇「No」
7. 選擇「All file types」
8. 輸入App name
9. 將產生的App key和App secret依以下格式建立apikey.json

		{	
			"key": "kkkkkkkkkkkkk",
 		    "secret": "sssssssssssss"
		}

### 執行

1. 執行dropbox_camera_uploads_bak.py [儲存目錄]，例：

		dropbox_camera_uploads_bak.py /tmp
		
2.	初次執行要到程式提示的網誌確認後取得authorization code並輸入進程式中

### 遇到問題

遇到問題請開issue囉