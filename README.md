Email Spam Classifier

📌 Project Description

Email Spam Classifier is a machine learning-based web application that automatically identifies whether an email or text message is Spam or Ham (Not Spam). The project uses TF-IDF for text feature extraction and the Multinomial Naive Bayes algorithm for classification. A Flask web interface allows users to enter a message and instantly receive the prediction result.

🚀 Features

- Classifies messages as Spam or Ham
- Uses TF-IDF for text feature extraction
- Uses Multinomial Naive Bayes machine learning algorithm
- Displays model accuracy and classification results
- Provides a simple web-based user interface
- Supports real-time message prediction

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- TF-IDF
- Multinomial Naive Bayes
- HTML
- CSS

⚙️ Project Workflow

Dataset
   ↓
Data Preprocessing
   ↓
TF-IDF Feature Extraction
   ↓
Train-Test Split
   ↓
Naive Bayes Model Training
   ↓
Message Prediction
   ↓
SPAM / HAM Result

📂 Project Structure

Email-Spam-Classifier/
│
├── app.py
├── data/
│   └── spam.csv
├── templates/
│   └── index.html
├── .gitignore
└── README.md

▶️ How to Run

1. Clone the repository.
2. Open the project folder in a terminal.
3. Create and activate a Python virtual environment.
4. Install the required packages.
5. Run the Flask application.

python app.py

6. Open the local Flask URL in a web browser.
7. Enter an email or message and click Check Message.

📊 Machine Learning Model

The project uses Multinomial Naive Bayes, which is suitable for text classification tasks. The input text is converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) before classification.

🎯 Applications

- Email spam detection
- SMS spam filtering
- Unwanted message identification
- Basic text classification systems

🔮 Future Enhancements

- Improve the user interface
- Add more training data
- Support multiple languages
- Deploy the application online
- Add additional machine learning models
- Provide prediction confidence scores

👩‍💻 Author

S. Asmiya
