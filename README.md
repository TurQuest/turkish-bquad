# Turkish-BQuAD: Biology Question Answering Dataset for Turkish Language

## Biz kimiz ?
Merhaba biz iki kişiyiz. Adlarımız [Kerem Berke](https://github.com/4c0a), [Ela Nur](https://github.com/ellanur). Biz, Pınar Koleji Fen Lisesinde okuyan ikiz kardeşleriz. Bilim fuarlarında artırılmış gerçeklik ve derin öğrenme konularında projeler ile katılımlar sağladık. Artırılmış gerçeklik projemiz ile dereceye girdik. Bu yazı değerlendirmek için Teknofest Doğal Dil İşleme yarışmasına hazırlanmak istedik.

Danışmanımız olan [Fatih Çağatay Akyön](https://github.com/fcakyon) ODTÜ'de doğal dil işleme üzerine doktora yapıyor. Derin öğrenme üzerine 5 tane patenti var ve 20'den fazla makale yayınladı. Aynı zamanda geliştirdiği açık kaynak derin öğrenme kütüphaneleri aylık 20 binden fazla kez indiriliyor.

## Projenin Motivasyonu
- Türkiye’de LGS ve TYT hazırlık test kitapları ve okul sınavları için öğretmenler her yıl yüz binlerce soru üretmektedirler. Benzer şekilde lise ve ortaokul öğrencileri yapamadıkları soruların cevaplarını konu anlatım metinlerinden bulup çalışmaktadırlar.

- Doğal Dil İşleme alanındaki son gelişmelerle birlikte soru cevaplama (question answering) modelleri ile metinlerden otomatik soru cevaplama, soru üretme (question generation) modelleri ile paragraflardan otomatik soru üretme mümkün hale gelmiştir.

- Ancak Türkçe dili için model eğitebilmek adına, Teknofest 2018 kapsamında paylaşılan TQuAD veriseti dışında herhangi bir soru/cevap veriseti bulunmamaktadır.

- Bu açığı kapatabilmek adına Biyoloji konusuyla ilgili bir soru/cevap veriseti hazırlamak istiyoruz.

## Soru Cevaplama (Question Answering)
Soru cevaplama, bir bilgi geri getirim sistemine yöneltilen sorulara cevap döndürülmesidir. Bu yaklaşımla geliştirilmiş bilgi geri getirim sistemi ise soru cevaplama sistemi olarak adlandırılır. Otomatik olarak metinden bir sorunun cevabının bulunması bu yöntem ile sağlanır.

## Cevap Çıkarma (Answer Extraction)
Bir metindeki cevap olabilecek kelime veya kelime gruplarının tespit edilmesi işlemine denir. T5, Bert, Electra gibi modellerin yaygınlaşmasıyla derin öğrenme ile otomatik cevap çıkarma işlemi mümkün hale geldi.

## Soru Üretme (Question Generation)
Verilen bir metinden, dil bilgisi açısından tutarlı sorular üğretilmesine denir. Günümüzde T5, GPT mimarili modellerin cümle üretme (generation) yeteneklerinin gelişmesiyle birlikte, derin öğrenme modelleri ile otomatik soru üretmek mümkün olmuştur.

## Veri seti / Dataset
Türkçe doğal dil işleme literatüründe halka açık olarak paylaşılmış sadece bir (TQuAD) soru-cevap seti mevcut. Türkçe NLP literatüründeki bu eksiği giderebilmek için Biyoloji dersi üzerinde odaklanmış bir soru-cevap seti paylaşıyoruz. Lise 1,2,3,4 sınıflarındaki MEB kitaplarındaki paragraflardan çıkarılmış metin/soru/cevaplardan oluşuyor. Biyoloji dersi üzerine cevap çıkarma, soru cevaplama ve soru üretme modellerinin eğitiminde kullanılabilecek bir veri seti olarak sunuyoruz. Yaygın olarak kullanılan [SQuAD v2.0](https://rajpurkar.github.io/SQuAD-explorer) formatında oluşturduk seti.

```json
            "paragraphs": [
                {
                    "qas": [
                        {
                            "question": "Bakterilerin neden zarlı hücre organelleri yoktur?",
                            "id": 117299,
                            "answers": [
                                {
                                    "text": "hücre içi zar sistemi oluşturamadığından",
                                    "answer_start": 85,
                                }
                            ],
                            "is_impossible": false
                        },
                        {
                            "question": "Bakterilerin sitoplazmasında küçük ve halkasal yapıda bulunan DNA parçalarına ne ad verilir?",
                            "id": 117307,
                            "answers": [
                                {
                                    "text": "plazmit",
                                    "answer_start": 217,
                                }
                            ],
                            "is_impossible": false
                        }
                    ],
                    "context": "Bakterilerin sitoplazmalarında dağınık hâlde bulunan halkasal DNA vardır. Bakteriler hücre içi zar sistemi oluşturamadığından zarlı hücre organelleri yoktur. Bazı bakterilerin sitoplazmasında küçük ve halkasal yapıda plazmit adı verilen DNA parçaları bulunur. Plazmitler, antibiyotiklere veya kimyasal maddelere karşı direnç kazandıran genler taşır. Bakteriler, pasif veya aktif şekilde hareket edebilir. Bakterilerde hücrelerin birbirine tutunmasını, haberleşmesini ve gen aktarımını sağlayan ve hücre zarının dışarıya doğru uzamasıyla oluşan pilus adı verilen uzantılar bulunur. Bazı bakterilerde aktif olarak yer değiştirmeyi sağlayan kamçı vardır.",
                }
            ]
```
|                          |  Paragraf / Paragraph | Soru-Cevap / Q&A |
|--------------------------|-----------------------|------------------|
| Doğrulama / Validation   | 40                    | 153              |
| Eğitim / Train           | 154                   | 618              |

## Deneyler
Paylaştığımız verisetinin kullanılabilirliğini göstermek amacıyla [Bert](https://arxiv.org/pdf/1810.04805.pdf) ve [T5](https://arxiv.org/pdf/2010.11934.pdf) modelleri üzerinde Soru Cevaplama (Question Answering), Cevap Çıkarma (Answer Extraction) ve Soru Üretme (Question Generation) modelleri eğittik.

618 soru-cevap'tan oluşan Turkish-BQuAD seti ile 14224 soru-cevap'tan oluşan TQuAD setinin Turkish-BQuAD doğrulama seti üzerindeki sonuçlarını kıyaslayabilmek için çeşitli eğitim seti kombinasyonlarında eğitimler yapıldı.

Sonuçları [F1](https://arxiv.org/pdf/1606.05250.pdf), [EM](https://arxiv.org/pdf/1606.05250.pdf), [BertScore](https://openreview.net/forum?id=SkeHuCVFDr), [BLEU](https://www.aclweb.org/anthology/C04-1072), [ROUGE](https://www.aclweb.org/anthology/W04-1013), [METEOR](https://www.aclweb.org/anthology/W05-0909) metrikleri üzerinden değerlendirdik.

## Sonuçlar

### Soru Cevaplama (Question Answering)

| Model                          |  Eğitim (Train) Seti  | F1               | EM               |
|--------------------------------|-----------------------|------------------|------------------|
| dbmdz/bert-base-turkish-cased  | Turkish-BQuAD         | 76.8             | 70.1             |
| dbmdz/bert-base-turkish-cased  | TQuAD                 | 82.7             | 70.3             |
| dbmdz/bert-base-turkish-cased  | Turkish-BQuAD + TQuAD | 88.4             | 79.1             |
|--------------------------------|-----------------------|------------------|------------------|
| google/mt5-small               | Turkish-BQuAD         | 80.6             | 74.3             |
| google/mt5-small               | TQuAD                 | 70.4             | 53.4             |
| google/mt5-small               | Turkish-BQuAD + TQuAD | 81.6             | 71.0             |

### Cevap Çıkarma (Answer Extraction)

| Model                          |  Eğitim (Train) Seti  | F1               | Precision        | BertScore        |
|--------------------------------|-----------------------|------------------|------------------|------------------|
| google/mt5-small               | Turkish-BQuAD         | 52.2             | 52.1             |66.2              |
| google/mt5-small               | TQuAD                 | 18.0             | 15.2             |49.1              |
| google/mt5-small               | Turkish-BQuAD + TQuAD | 43.6             | 42.3             |64.4              |

### Soru Üretme (Question Generation)

| Model                          |  Eğitim (Train) Seti  | BLEU1   | BLEU2   | BLEU3   | BLEU4   | ROUGE-L | METEOR  | BertScore |
|--------------------------------|-----------------------|---------|---------|---------|---------|---------|---------|-----------|
| google/mt5-small               | Turkish-BQuAD         | 75.4    | 72.4    | 70.0    | 67.8    | 73.7    | 70.6    | 79.5      |
| google/mt5-small               | TQuAD                 | 57.2    | 52.3    | 48.9    | 46.1    | 59.4    | 52.3    | 81.7      |
| google/mt5-small               | Turkish-BQuAD + TQuAD | 74.4    | 70.7    | 67.8    | 65.3    | 74.5    | 72.2    | 86.7      |
