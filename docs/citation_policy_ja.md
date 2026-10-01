# BIG 引用方針

このページは、**Boundary Information Geometry（BIG）** を、主張の証拠レベルに合わせて引用するための方針です。

BIGリポジトリは一つの論文ではなく、複数のB-seriesからなる研究プログラムです。したがって、引用先も主張の種類に合わせて分けます。

基本ルールは次です。

```text
repository / documentationについて述べる
    -> GitHub repositoryを引用

programme全体の研究状況を述べる
    -> 対応するstatus recordを引用

特定の数値結果・構造結果を述べる
    -> その結果を報告したB-seriesのZenodo論文を引用
```

特定の数値結果を、repository全体の引用だけで代用しないことを推奨します。

---

## 1. Repository全体を引用する場合

次のような場合はGitHub repositoryを引用します。

- BIGを研究プログラムとして紹介する場合
- repository構成について述べる場合
- living documentationを参照する場合
- 現在の統合research status mapを参照する場合
- code / documentationのrepository-level provenanceを示す場合

推奨形式:

```text
Lucis, J. Boundary Information Geometry (BIG). GitHub repository.
https://github.com/Jun-Lucis/BIG-theory
```

特定時点のrepository状態を再現可能に示す必要がある場合は、Git commit SHAも併記してください。

machine-readableなrepository citationは [../CITATION.cff](../CITATION.cff) にあります。

---

## 2. Programme-level synthesisを引用する場合

複数B-seriesを横断してBIGの証拠状況を論じる場合は、対応するprogramme-level recordを使います。

### B23までの歴史的programme status

**DOI:** https://doi.org/10.5281/zenodo.22939024

これはB23までのarchived status snapshotです。後のB23AやB24–B26を含む文書として扱わないでください。

### B23A structural-universality audit

**DOI:** https://doi.org/10.5281/zenodo.22994445

P1–P6のprospective universality audit、およびstructural/formal universalityとquantitative universalityの区別を論じる場合に使います。

### B24–B25 Phase I

**DOI:** https://doi.org/10.5281/zenodo.22956894

cross-sector auditと、最初のprospectiveに成功したlevel-resolved transfer constructionを論じる場合に使います。

### B25 Phase II

**DOI:** https://doi.org/10.5281/zenodo.22967474

family-restrictedなfixed perimeter coefficientへの縮約を論じる場合に使います。

### B26

**DOI:** https://doi.org/10.5281/zenodo.22972985

topology-localized two-center transfer testと、terminal fixed-coefficient geometry-transfer failureを論じる場合に使います。

B3–B26＋B23Aのbaseline living synthesisは次です。

- [research_status_map_B3_B26_ja.md](research_status_map_B3_B26_ja.md)
- [research_status_map_B3_B26.md](research_status_map_B3_B26.md)

B27–B36の後期statusは次です。

- [research_status_update_B27_B36_ja.md](research_status_update_B27_B36_ja.md)
- [research_status_update_B27_B36.md](research_status_update_B27_B36.md)

これらはliving GitHub documentなので、厳密な文面を引用する場合はrepositoryとcommit SHAを併記することを推奨します。

---

## 3. 特定の数値結果・構造結果を引用する場合

一つのB-seriesの実験に依存する主張は、**その結果を直接報告したZenodo paper / record** を引用します。

例:

- B9のfission-like metastability -> B9 record
- B20のresponse-normal result -> B20 record
- B21のlocal kinematic closure -> B21 record
- B22のprospective geometry -> B22 record
- B23のcross-branch result -> B23 record
- B23A P1–P6 universality audit -> B23A record
- B26のfixed-coefficient transfer failure -> B26 record
- B27のhistory-conditioned response / reconfiguration-covariance result -> DOI https://doi.org/10.5281/zenodo.23024324
- B28のlineage-transport failureまたはB29のtraining-domain readability stop -> B28–B29統合record、DOI https://doi.org/10.5281/zenodo.23050390
- B30–B36のresponse-to-pulse-timing result -> DOI https://doi.org/10.5281/zenodo.23048197

canonical DOI listは [publication_map.md](publication_map.md) にあります。

negative、inconclusive、implementation-invalid、resolution-sensitiveな結果に依存する主張では、その状態を保存しているrecordを引用し、後のpositive resultで置き換えないでください。

---

## 4. 複合的な主張の引用階層

programme全体の解釈と特定の数値を同じ文章で扱う場合は、両方を引用します。

```text
programme-level interpretation
    -> 対応するBIG status record

specific numerical statement
    -> その数値を生成したB-series paper
```

これにより、

1. broad status documentを、すべての数値のprimary sourceとして使うこと
2. 一つのsuccessful B-series paperを、programme-wide universal claimの根拠として使うこと

の両方を避けられます。

---

## 5. 現在のclaim boundaryと引用

現在のrepositoryでは、次を区別します。

- **structural universality** — boundary、response、history、branch、reconfigurationという構造的組織
- **formal universality** — 異なる系で比較可能な数学対象を定義できること
- **quantitative universality** — 同じ数値predictor、coefficient、reset amplitude、rate lawなどが異なる系でもtransferすること

現在の証拠がprogramme-levelで支持する最も強い統一的表現は、formal / structural comparabilityです。**一つの普遍的定量BIG lawは確立していません。**

引用でもこの区別を保持してください。

---

## 6. 著者とrepository

**Author:** Jun Lucis  
**Repository:** https://github.com/Jun-Lucis/BIG-theory

各paper title、version、file、DOIについては [publication_map.md](publication_map.md) を参照してください。
