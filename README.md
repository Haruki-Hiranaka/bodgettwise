# 💰 BudgetWise（バジェットワイズ）- 日本語UIの個人資産管理アプリ

BudgetWiseは、PythonとFlaskで構築された**シンプルかつ拡張性のある家計簿Webアプリ**です。
ブラウザから簡単に収入・支出を記録し、合計金額や残高をリアルタイムで可視化します。

---

## 🧩 主な特徴

### ✅ 大きなアピールポイント
- **PythonとFlaskだけで構築された軽量なWebアーキテクチャ**
- **データ永続化はCSVベースのため、導入が極めて簡単でローカル完結**

### ✨ 小さな工夫
- 日本語UIによる直感的な入力・集計体験
- データは即時反映、残高の自動再計算を実装
- レスポンシブなCSS設計でスマホでも見やすい

---

## 📸 画面イメージ（※ダミー）

![ホーム画面](images/sample_home.png)
![収支追加フォーム](images/sample_form.png)

---

## 🚀 セットアップ方法

```bash
git clone https://github.com/yourname/budgetwise.git
cd budgetwise
pip install -r requirements.txt
python src/app.py
```

起動後、ブラウザで `http://localhost:5000` にアクセス。

---

## 🔧 使用技術

| 技術      | 用途                 |
|-----------|----------------------|
| Python    | アプリケーションロジック |
| Flask     | Webアプリフレームワーク  |
| HTML/CSS  | UI構築              |
| CSV       | データ永続化（ローカル）|

詳細は [`ARCHITECTURE.md`](./ARCHITECTURE.md) をご覧ください。

---

## 🛠️ 今後の機能追加候補

- ユーザー別ログイン機能
- SQLiteやPostgreSQLへの切替
- グラフによる月別分析・カテゴリ集計

---

## 📄 ライセンス

MIT License
