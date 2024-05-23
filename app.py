import streamlit as st
import seaborn as sns

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Main function to run the Streamlit app
def main():
    st.title('Iris Dataset Exploration')

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
            iris_df.columns.tolist(),
            default=["sepal_length", "sepal_width", "petal_length", "petal_width"]
        )
        
        # Generate pairplot based on selected features
        if len(selected_features) > 1:
            sns.pairplot(iris_df[selected_features])
            st.pyplot()
        else:
            st.warning("Please select at least two features for pairplot.")

if __name__ == "__main__":
    main()
