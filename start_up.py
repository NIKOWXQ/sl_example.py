import streamlit as st

def main():
    st.title("File Upload App")
    
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "json", "py"])

    if uploaded_file is not None:
        st.write("### File Content:")
        
        # Read and display the file content
        try:
            content = uploaded_file.read().decode("utf-8")
            st.text_area("File Content:", content, height=300)
        except Exception as e:
            st.error(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
