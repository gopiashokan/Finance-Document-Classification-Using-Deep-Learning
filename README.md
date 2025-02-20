# Financial Document Classification using Deep Learning

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1t6wJ5SA7qiaZ813TWlcEg0te9DAe6lN4?usp=sharing)

**Introduction**

Managing and classifying financial documents manually is both time-consuming and error-prone. This project streamlines the process by leveraging deep learning techniques for automated classification. Utilizing TensorFlow and fine-tuning the FinBERT model on a custom dataset, we achieve precise categorization of financial documents. The model is seamlessly integrated into a user-friendly Streamlit application and deployed on the Hugging Face platform, ensuring high accuracy and efficiency in financial document management.

<br />

**Table of Contents**

1. Key Technologies and Skills
2. Installation
3. Usage
4. Features
5. Contributing
6. License
7. Contact

<br />

**Key Technologies and Skills**
- Python
- scikit-learn
- TensorFlow
- Transformers
- Numpy
- Pandas
- BeautifulSoup
- Matplotlib
- Seaborn
- Streamlit
- Hugging Face

<br />

**Installation**

To run this project, you need to install the following packages:

```python
pip install python-dotenv
pip install datasets
pip install tensorflow
pip install transformers
pip install sentencepiece
pip install numpy
pip install pandas
pip install beautifulsoup4
pip install matplotlib
pip install seaborn
pip install streamlit
pip install streamlit_extras
pip install huggingface-hub
```

**Note:** If you face "ImportError: DLL load failed" error while installing TensorFlow,
```python
pip uninstall tensorflow
pip install tensorflow==2.12.0 --upgrade
```

<br />

**Usage**

To use this project, follow these steps:

1. Clone the repository: ```git clone https://github.com/gopiashokan/Finance-Document-Classification-Using-Deep-Learning.git```
2. Install the required packages: ```pip install -r requirements.txt```
3. Run the Streamlit app: ```streamlit run app.py```
4. Access the app in your browser at ```http://localhost:8501```

<br />

**Features**

#### Data Collection:
   The dataset comprises HTML files organized into five distinct folders, namely Balance Sheets, Cash Flow, Income Statement, Notes, and Others. These folders represent various financial document categories. You can access the dataset via the following download link.

📙 Dataset Link: [https://www.kaggle.com/datasets/gopiashokan/financial-document-classification-dataset](https://www.kaggle.com/datasets/gopiashokan/financial-document-classification-dataset)


#### Data Preprocessing:

   - **Text Extraction:** BeautifulSoup is utilized to parse and extract text content from HTML files. The extracted text is structured into a DataFrame using Pandas, and the target labels are encoded to facilitate numerical processing for model training.

   - **Data Splitting:** The dataset was divided into training and testing sets using a Scikit-learn. This partitioning strategy ensured an appropriate distribution of data for model training and evaluation, thereby enhancing the robustness of the trained model.

   - **Tokenization:** The **FinBERT** tokenizer from Hugging Face Transformers library `yiyanghkust/finbert-pretrain` is applied to convert text data into numerical vectors, enabling the model to process financial terminology effectively.

   - **Padding and Truncation:** Tokenized sequences are padded and truncated to a maximum length of 512, ensuring consistent input sizes both training and testing datasets.


#### Model Training:

   - **Pretrained Model:** The FinBERT is a domain-specific BERT model for financial texts, is loaded and **Fine-tuned** using Transfer Learning on the custom dataset for improving classification accuracy.

   - **Optimization Strategy:** The model is compiled using the `Adam` optimizer, `SparseCategoricalCrossentropy` loss function, and `Accuracy` as the evaluation metric, optimizing performance across multiple financial document classes.

   - **Training and Evaluation:** The model is trained and validated using TensorFlow, achieving a classification accuracy of **95.84%**, demonstrating its effectiveness in financial document classification.

![](https://github.com/gopiashokan/Finance-Document-Classification-Using-Deep-Learning/blob/main/image/Accuracy_Loss_Graph.jpg)


#### Model Deployment and Inference:

   - **Hugging Face Hub Integration:** The Fine-tuned model and tokenizer are deployed on the Hugging Face Hub using Access Token, allowing easy accessibility and inference through APIs.
     <br> *Hugging Face Hub:* [https://huggingface.co/gopiashokan/Financial-Document-Classification-using-Deep-Learning](https://huggingface.co/gopiashokan/Financial-Document-Classification-using-Deep-Learning)

   - **Application Development:** A user-friendly Streamlit application was developed to allow users to upload new HTML documents for classification. The application provided a simple interface for users to interact with, displaying the predicted class and associated confidence scores. Additionally, the application showcased the uploaded document, enhancing the interpretability of the classification results.

   - **API-based Inference:** The Streamlit application was deployed on the Hugging Face platform, enabling easy access for users to utilize the model for document classification. By deploying on Hugging Face, users can seamlessly upload new HTML documents and sends extracted text to the Hugging Face API, retrieves model predictions and displays the highest confidence class along with its score.

![](https://github.com/gopiashokan/Finance-Document-Classification-Using-Deep-Learning/blob/main/image/Inference.png)

🚀 **Application:** [https://huggingface.co/spaces/gopiashokan/Financial-Document-Classification-using-Deep-Learning](https://huggingface.co/spaces/gopiashokan/Financial-Document-Classification-using-Deep-Learning)


<br />


**Conclusion:**

This project successfully classifies financial documents using deep learning and transfer learning techniques. By leveraging FinBERT and fine-tuning it on a domain-specific dataset, we achieve high accuracy in document categorization. The integration of a user-friendly Streamlit application enhances accessibility, making financial document classification more efficient and scalable.

<br />

**References:**

   - scikit-learn Documentation: [https://scikit-learn.org/](https://scikit-learn.org/)
   - TensorFlow Documentation: [https://www.tensorflow.org/](https://www.tensorflow.org/)
   - Transformers Documentation: [https://huggingface.co/docs/transformers/en/index](https://huggingface.co/docs/transformers/en/index)
   - Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)

<br />

**Contributing:**

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

<br />

**License:**

This project is licensed under the MIT License. Please review the LICENSE file for more details.

<br />

**Contact:**

📧 Email: gopiashokankiot@gmail.com 

🌐 LinkedIn: [linkedin.com/in/gopiashokan](https://www.linkedin.com/in/gopiashokan)

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.

