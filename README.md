# product-recommendation
This repository features a Product Recommendation Dashboard using Python and Streamlit. It leverages the Online Retail dataset, containing UK retail transaction data, to provide personalized product suggestions. By employing content-based filtering, the dashboard demonstrates the use of machine learning in enhancing retail experiences.

**Dataset Details**

The dataset used is the Online Retail dataset, which includes the following key attributes:


InvoiceNo: Unique identifier for each transaction.

StockCode: Product identifier.

Description: Description of the product.

Quantity: Quantity of the product purchased.

InvoiceDate: Date and time of the transaction.

UnitPrice: Price of the product per unit.

CustomerID: Unique identifier for each customer.

Country: Country where the customer resides.


**How It Works**

Data Loading and Preprocessing:The dataset is read into a pandas DataFrame, and relevant features like Description and CustomerID are used to build a content-based recommendation model.

Recommendation Model: The system combines product descriptions into a single text representation, applies TF-IDF Vectorization to transform the text into numerical feature vectors, and computes cosine similarity to identify similar products. Recommendations are generated based on similarity scores, excluding items the user has already purchased.

Interactive Dashboard: Users can input their Customer ID to receive personalized recommendations. The dashboard also displays a sample of the dataset and provides feedback if the entered ID does not exist in the dataset.

**Libraries Used**

Streamlit: For creating the interactive dashboard.

pandas: For data manipulation and preprocessing.

scikit-learn: For implementing TF-IDF vectorization and cosine similarity.

numpy: For numerical computations.

openpyxl: For reading Excel files.


**Steps to Run the Project**

Clone the Repository:

Clone this repository to your local machine using:

bash

Copy code

git clone <repository_url>

Prepare the Environment:

Ensure Python 3.10 or higher is installed. Install the required dependencies using the command:

bash

Copy code

pip install -r requirements.txt

Add the Dataset:
Place the Online Retail dataset (Online Retail.xlsx) in the root directory of the project.

Run the Dashboard:
Launch the Streamlit application by running:

bash

Copy code

streamlit run recommendation_dashboard.py

Access the Dashboard:

Open your browser and navigate to the local URL provided in the terminal, typically http://localhost:8501.

Interact with the Dashboard:
Enter a valid Customer ID to get product recommendations, or explore the dataset using the provided interface.

**Future Enhancements**

Future iterations of this project could include:

Adding collaborative filtering techniques to complement the content-based model,
Enabling real-time data updates for live systems,
Providing richer visualizations to understand user behavior and product trends.
