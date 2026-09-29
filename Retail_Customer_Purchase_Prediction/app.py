import streamlit as st
import pandas as pd
import joblib

# Model load
model = joblib.load("retail_purchase_model.pkl")

st.title("🛒 Retail Customer Purchase Prediction")

st.write(
    "Customer ki website activity enter karo aur dekho "
    "ki customer purchase karega ya nahi."
)

# Customer details
Administrative = st.number_input("Administrative Pages", min_value=0, value=0)

Administrative_Duration = st.number_input(
    "Administrative Duration", min_value=0.0, value=0.0
)

Informational = st.number_input(
    "Informational Pages", min_value=0, value=0
)

Informational_Duration = st.number_input(
    "Informational Duration", min_value=0.0, value=0.0
)

ProductRelated = st.number_input(
    "Product Related Pages", min_value=0, value=1
)

ProductRelated_Duration = st.number_input(
    "Product Related Duration", min_value=0.0, value=0.0
)

BounceRates = st.number_input(
    "Bounce Rate", min_value=0.0, value=0.02
)

ExitRates = st.number_input(
    "Exit Rate", min_value=0.0, value=0.02
)

PageValues = st.number_input(
    "Page Values", min_value=0.0, value=0.0
)

SpecialDay = st.number_input(
    "Special Day", min_value=0.0, max_value=1.0, value=0.0
)

Month = st.selectbox(
    "Month",
    ["Aug", "Dec", "Feb", "Jul", "June", "Mar", "May", "Nov", "Oct", "Sep"]
)

OperatingSystems = st.number_input(
    "Operating System", min_value=1, value=2
)

Browser = st.number_input(
    "Browser", min_value=1, value=2
)

Region = st.number_input(
    "Region", min_value=1, value=1
)

TrafficType = st.number_input(
    "Traffic Type", min_value=1, value=2
)

VisitorType = st.selectbox(
    "Visitor Type",
    ["Returning_Visitor", "New_Visitor", "Other"]
)

Weekend = st.selectbox(
    "Weekend",
    ["False", "True"]
)


# Encoding
month_mapping = {
    "Aug": 0,
    "Dec": 1,
    "Feb": 2,
    "Jul": 3,
    "June": 4,
    "Mar": 5,
    "May": 6,
    "Nov": 7,
    "Oct": 8,
    "Sep": 9
}

visitor_mapping = {
    "New_Visitor": 0,
    "Other": 1,
    "Returning_Visitor": 2
}

weekend_mapping = {
    "False": 0,
    "True": 1
}


if st.button("Predict Purchase"):

    input_data = pd.DataFrame([[
        Administrative,
        Administrative_Duration,
        Informational,
        Informational_Duration,
        ProductRelated,
        ProductRelated_Duration,
        BounceRates,
        ExitRates,
        PageValues,
        SpecialDay,
        month_mapping[Month],
        OperatingSystems,
        Browser,
        Region,
        TrafficType,
        visitor_mapping[VisitorType],
        weekend_mapping[Weekend]
    ]], columns=[
        "Administrative",
        "Administrative_Duration",
        "Informational",
        "Informational_Duration",
        "ProductRelated",
        "ProductRelated_Duration",
        "BounceRates",
        "ExitRates",
        "PageValues",
        "SpecialDay",
        "Month",
        "OperatingSystems",
        "Browser",
        "Region",
        "TrafficType",
        "VisitorType",
        "Weekend"
    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("🛒 Customer Purchase karega")
    else:
        st.info("❌ Customer Purchase nahi karega")

    st.write(
        "Purchase Probability:",
        round(probability * 100, 2),
        "%"
    )

    if probability < 0.30:
        st.warning("Low Purchase Intent")
    elif probability < 0.70:
        st.info("Medium Purchase Intent")
    else:
        st.success("High Purchase Intent")