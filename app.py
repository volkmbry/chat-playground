import streamlit as st
import pandas as pd

# Load the Iris dataset
def load_iris_dataset():
    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv"
    return pd.read_csv(url)

# Main function to run the Streamlit app
def main():
    st.title('Iris Dataset Exploration')

    # Load dataset
    iris_df = load_iris_dataset()

    st.subheader('Dataset Preview')
    st.write(iris_df.head())

    # Display options
    display_option = st.sidebar.radio(
        "Choose how to display the data:",
        ('Table', 'Pairplot')
    )

    if display_option == 'Table':
        st.subheader('Iris Data Table')
        st.write(iris_df)
    
    elif display_option == 'Pairplot':
        st.subheader('Pairplot of Iris Dataset')
        
        # Select features for pairplot
        selected_features = st.sidebar.multiselect(
            "Select features for pairplot:",
            iris_df.columns.tolist()[:-1],  # Exclude the target variable
            default=["sepal_length", "sepal_width", "petal_length", "petal_width"]
        )
        
        # Generate pairplot based on selected features
        if len(selected_features) > 1:
            st.write("Pairplot with selected features:", selected_features)
            st.write("Please note: Streamlit does not support pairplot directly. You may need to use an alternative visualization library.")
        else:
            st.warning("Please select at least two features for pairplot.")

if __name__ == "__main__":
    main()
