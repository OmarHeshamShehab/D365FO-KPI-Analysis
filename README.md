# D365FO KPI Dashboard

## Project Description
The **D365FO KPI Dashboard** is a Streamlit-based web application designed to visualize key performance indicators (KPIs) from Microsoft Dynamics 365 Finance and Operations (D365FO) using its OData API. This dashboard provides an interactive interface to explore and analyze data from multiple entities, including Vendors, Customers, and Sales Orders. It leverages secure Azure AD authentication to fetch real-time data and presents it through intuitive tables and visualizations powered by Plotly. The application is ideal for business analysts, data engineers, and D365FO administrators looking to monitor and derive insights from operational data efficiently.

## Features
- **Multi-Entity Support**: Displays KPIs for Vendors (VendorsV2), Customers (CustomersV3), and Sales Orders (SalesOrderHeadersV2) in separate tabs.
- **Interactive Visualizations**: Includes bar charts, line charts, pie charts, and histograms to represent data trends and distributions.
- **Secure Authentication**: Uses Azure AD client credentials flow to securely authenticate and access the D365FO OData API.
- **Real-Time Data Fetching**: Retrieves the latest data from D365FO with configurable query limits (default: top 100 records).
- **Responsive Design**: Built with Streamlit's wide layout for an optimized viewing experience.
- **Error Handling**: Gracefully handles API errors and displays meaningful messages to the user.

## Prerequisites
To run this project, ensure you have the following:
- **Python 3.8+** installed.
- A **Microsoft Dynamics 365 Finance and Operations** instance with OData API access enabled.
- An **Azure AD application** registered with the necessary permissions to access the D365FO OData API.
- A `.env` file configured with the required environment variables (see [Environment Variables](#environment-variables)).
- A local or cloud environment to host the Streamlit application.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/d365fo-kpi-dashboard.git
   cd d365fo-kpi-dashboard
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add the following:
   ```plaintext
   AZURE_TENANT_ID=your-tenant-id
   AZURE_CLIENT_ID=your-client-id
   AZURE_CLIENT_SECRET=your-client-secret
   D365_BASE_URL=your-d365fo-base-url
   ```
   Replace the placeholders with your Azure AD and D365FO instance details.

5. **Run the Application**:
   ```bash
   streamlit run streamlit_app.py
   ```
   The application will open in your default web browser at `http://localhost:8501`.

## Usage
1. **Access the Dashboard**:
   - Open the application in your browser.
   - The dashboard is divided into three tabs: Vendors, Customers, and Sales Orders.

2. **Explore KPIs**:
   - **Vendors Tab**: View vendor data, including a bar chart of vendors created by user and a line chart of vendors created over time.
   - **Customers Tab**: Analyze customer data with a pie chart of customer groups and a line chart of customers created over time.
   - **Sales Orders Tab**: Examine sales order data with a bar chart of order statuses and a histogram of order total amounts.

3. **Interact with Visualizations**:
   - Hover over charts to see detailed data points.
   - Use Streamlit's interactive features to filter or expand tables and charts.

## Project Structure
```
d365fo-kpi-dashboard/
├── odata_client.py       # Handles OData API authentication and data fetching
├── streamlit_app.py      # Main Streamlit application with dashboard logic
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not tracked in git)
└── README.md             # Project documentation
```

## Environment Variables
The `.env` file must include the following variables:
- `AZURE_TENANT_ID`: Your Azure AD tenant ID.
- `AZURE_CLIENT_ID`: The client ID of the registered Azure AD application.
- `AZURE_CLIENT_SECRET`: The client secret for the Azure AD application.
- `D365_BASE_URL`: The base URL of your D365FO instance (e.g., `https://your-instance.dynamics.com`).

**Note**: Keep the `.env` file secure and do not commit it to version control.

## Dependencies
The project relies on the following Python packages (listed in `requirements.txt`):
- `requests`: For making HTTP requests to the OData API.
- `pandas`: For data manipulation and DataFrame creation.
- `streamlit`: For building the web-based dashboard.
- `plotly`: For creating interactive visualizations.
- `python-dotenv`: For loading environment variables from a `.env` file.

## Security Notes
- The `odata_client.py` script disables SSL verification (`verify=False`) for simplicity. In a production environment, ensure proper SSL certificate validation to avoid security risks.
- Store sensitive credentials (e.g., `AZURE_CLIENT_SECRET`) securely and avoid hardcoding them in the source code.
- Restrict Azure AD application permissions to the minimum required for OData API access.

## Limitations
- The application fetches only the top 100 records per entity by default. Modify the `top` parameter in `fetch_odata_entity` to retrieve more data.
- Visualizations depend on specific columns (e.g., `CreatedBy`, `CreatedDateTime`, `SalesOrderStatus`) being present in the OData response. Ensure your D365FO instance includes these fields.
- Large datasets may impact performance due to the in-memory processing of Pandas DataFrames.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description of your changes.

## Contact
For questions or support, please open an issue on the GitHub repository.