import streamlit as st



# Define a function to display the signature
def display_signature():
    st.markdown(
                """
                    <style>
                            .signature {
                                font-size: 1rem;
                                font-style: italic;
                                text-align: center;
                                padding: 1rem 0;
                                color: #333;
                                transition: color 0.5s ease-in-out;
                            }
                            .signature:hover {
                                color: #007bff;
                            }
                    </style>
                """
        , unsafe_allow_html=True
    )
    st.markdown(
        """
            <div class="signature">
                Made with ❤️ by Shib Kumar Saraf
            </div>
        """
        , unsafe_allow_html=True
    )
