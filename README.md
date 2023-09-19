# Missing Parts Reporter

The Missing Parts Reporter is a Django web application designed to streamline the process of reporting missing parts for appliances. This application allows users to input crucial information including the missing part's details, SKU, the appliance's location in the store, and the order number for the purchased missing part. The system then automatically generates a QR code that encapsulates all the provided data for convenient tracking.

## Features

- Report missing parts for appliances with ease.
- Automatically generate QR codes containing relevant information.
- Provide feedback directly to the developer for improvements.

## Installation

Follow these steps to set up and run the Missing Parts Reporter on your local system:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Elkrypton/orders_reporter.git
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations**:

    ```bash
    python manage.py migrate
    ```

4. **Start the Development Server**:

    ```bash
    python manage.py runserver
    ```

5. **Access the Application**:

    Open your web browser and go to [http://localhost:8000](http://localhost:8000) to use the application.

## Usage

1. Navigate to the home page.
2. Click on "Report Missing Part".
3. Fill in the following details:
   - Missing Part
   - SKU
   - Location in Store
   - Order Number
4. The QR code containing the entered information will be automatically generated and could be placed on the appliance.
5. Optionally, you can provide feedback to the developer using the "Feedback" option in the navigation menu.

## Feedback

If you have any feedback or encounter any issues, please feel free to [create an issue](https://github.com/Elkrypton/orders_reporter/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- QR code generation functionality powered by [qrcode library](https://github.com/lincolnloop/python-qrcode).

## Author

Rochdi El Majdoub
Email: rochdielmajdoub@gmail.com

## Contributing

If you'd like to contribute to this project, please follow the [contributing guidelines](CONTRIBUTING.md).

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/missing-parts-reporter/tags).

## Disclaimer

This application is provided as-is, without any warranty or support. Use at your own risk.

