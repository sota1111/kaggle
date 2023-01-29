# link
[databricks](https://dbc-2eb2ee3e-ce16.cloud.databricks.com/?o=7819807711010255#)

# signateの使い方
https://pypi.org/project/signate/
- 投稿可能なコンペ
``` $ signate list ``` 
コンペが提供するファイル一覧
``` signate files --competition-id= ```
コンペが提供するファイルダウンロード
``` signate download --competition-id= ```

# databricksの使い方
df = spark.table("main.db_fdua_org.train").toPandas()
機械学習モデルは共通のモデルを用いる。
import xgboost as xgb

特定のgidに対して一行のデータを作る。

target_flagは2ヶ月連続で延滞する場合に1。
延滞予測であり、延滞時のデータは表示されない。