import pickle
import re
import nltk
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(stop_words='english')

nltk.download('punkt')
nltk.download('stopwords')

# Loading the model
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf_model = pickle.load(open('tfidf.pkl', 'rb'))

def clean_this_resume(txt):
    clean_text = re.sub('http\S+\s*', ' ', txt)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text











def main():
    st.title("Resume Classifier Website")
    upload_file = st.file_uploader("Upload Your Resume", type=['pdf', 'docx', "txt"])

    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_txt = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_txt = resume_bytes.decode('latin-1')

        cleaned_resume = clean_this_resume(resume_txt)
        vector = tfidf_model.transform([cleaned_resume])
        prediction = clf.predict(vector)[0]

        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }
        category_name = category_mapping.get(prediction, 'Unknown')

        st.write(f"The predicted Resume category is {category_name}")


if __name__ == '__main__':
     main()
