# 🎬 Movie Recommendation System (Content-Based Filtering)

This project is a **Content-Based Movie Recommendation System** that suggests similar movies based on a user’s selected movie. It uses **movie metadata**, **text vectorization**, and **cosine similarity** to generate accurate recommendations. The system is deployed using **Streamlit**, providing a fast, interactive, and user-friendly web interface without relying on any external APIs.

**APP LINK:https://movierecommendation-7eikhtkh8bd8fowafhckve.streamlit.app/**
---

## 📌 1. Project Objective

The main goal of this project is to:

* Recommend movies similar to a user-selected movie
* Use only movie content (not user ratings or history)
* Build a lightweight, fast, and scalable recommendation system
* Deploy the model as a web application using Streamlit

---

## 📌 2. Dataset Description

The dataset contains movie-related metadata such as:

* **Movie Title**
* **Genres**
* **Overview / Description**
* **Keywords**
* **Cast**
* **Crew (Director)**

These features are essential because they describe the *content* of a movie, which forms the basis of content-based filtering.

---

## 📌 3. Data Preprocessing (Step-by-Step)

### 🔹 Step 1: Data Cleaning

* Removed duplicate movie entries
* Handled missing values in important columns
* Selected only relevant columns required for recommendations

### 🔹 Step 2: Feature Engineering

* Combined multiple features (genres, overview, keywords, cast, crew) into a single column called **tags**
* Converted all text to lowercase for consistency

Example:

> tags = genres + overview + keywords + cast + director

---

## 📌 4. Text Vectorization

To convert text data into numerical format:

* Used **CountVectorizer** (Bag of Words model)
* Limited maximum features to reduce noise
* Removed common English stopwords

This converts movie descriptions into numerical vectors that machines can understand.

---

## 📌 5. Similarity Calculation

* Applied **Cosine Similarity** on vectorized movie data
* Cosine similarity measures the angle between two vectors
* Higher cosine similarity = more similar movies

This step creates a **similarity matrix** where each movie is compared with every other movie.

---

## 📌 6. Recommendation Logic

### 🔹 How recommendations work:

1. User selects a movie
2. The system finds the index of the selected movie
3. Retrieves similarity scores from the similarity matrix
4. Sorts movies based on similarity score
5. Returns the **top 5 most similar movies**

This approach ensures recommendations are relevant and content-focused.

---

## 📌 7. Model Optimization

* Precomputed similarity matrix for faster response
* Stored vectors and similarity data using **pickle**
* Avoided external API calls to improve speed and reliability

---

## 📌 8. Streamlit Web Application

The project is deployed using **Streamlit**, offering:

* Dropdown to select a movie
* Button to generate recommendations
* Clean and minimal UI
* Instant movie suggestions

### 🔹 Why Streamlit?

* Easy deployment
* Interactive UI
* Python-based
* Fast prototyping

---

## 📌 9. Project Workflow Summary

1. Load dataset
2. Clean and preprocess data
3. Create combined text features
4. Vectorize text data
5. Compute cosine similarity
6. Build recommendation function
7. Deploy using Streamlit

---

## 📌 10. Key Features

✅ Content-based filtering
✅ No external API dependency
✅ Fast recommendations
✅ Scalable and lightweight
✅ User-friendly interface

---

## 📌 11. Technologies Used

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle**

---

## 📌 12. Future Enhancements

* Add movie posters
* Implement hybrid recommendation system
* Improve NLP using TF-IDF or word embeddings
* Add user-based personalization

---

## 📌 13. Conclusion

This Movie Recommendation System demonstrates how **machine learning and NLP techniques** can be effectively used to build real-world recommender systems. The project focuses on simplicity, speed, and accuracy while maintaining a clean and deployable architecture.

---

⭐ *If you like this project, don’t forget to give it a star on GitHub!*

