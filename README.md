
# Vendor Management System

This project is backend for Vendor Management System. This project has various APIs protected with JSON Web Token.

## API Reference


```
  POST /api/token/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username`| `string` | **Required**. User's username/email. |
| `password`| `string` | **Required**. User's password. |

Description:
Generates a JSON Web Token (JWT) pair consisting of an access token and a refresh token for authentication.

---

Explanation:
- This endpoint is used to obtain JWT tokens for authentication.
- It accepts a POST request with the user's username/email and password in the request body.
- Upon successful authentication, it returns a JSON response containing the access token and refresh token.
- The access token can be used for authentication in subsequent requests to the API.
- The refresh token can be used to obtain a new access token when the current access token expires.
- Both the access token and refresh token are required for secure and continuous authentication.


```
  GET /api/vendors/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Bearer token obtained from the token endpoint. |

Description:
Retrieves a list of vendors.

---

```
  POST /api/vendors/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Bearer token obtained from the token endpoint. |

| Body Parameter     | Type     | Description                       |
| :----------------- | :------- | :-------------------------------- |
| `name`             | `string` | **Required**. Vendor's name.     |
| `contact_details`  | `string` | **Required**. Contact information of the vendor. |
| `address`          | `string` | **Required**. Physical address of the vendor. |
| `vendor_code`      | `string` | **Required**. A unique identifier for the vendor. |
| `on_time_delivery_rate` | `float` | **Optional**. Percentage of on-time deliveries. |
| `quality_rating_avg` | `float` | **Optional**. Average rating of quality based on purchase orders. |
| `average_response_time` | `float` | **Optional**. Average time taken to acknowledge purchase orders. |
| `fulfillment_rate` | `float` | **Optional**. Percentage of purchase orders fulfilled successfully. |

Description:
Creates a new vendor. Requires authentication using a Bearer token obtained from the token endpoint.

---

Explanation:
- For the `GET /api/vendors/` endpoint, you need to include the Bearer token obtained from the token endpoint in the Authorization header of the request.
- For the `POST /api/vendors/` endpoint, you need to include the Bearer token obtained from the token endpoint in the Authorization header of the request. Additionally, you need to provide the required information for creating a new vendor in the request body.


```
  GET /api/vendors/<int:id>/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `id`           | `integer`| **Required**. Unique identifier of the vendor. |

Description:
Retrieves details of a specific vendor identified by its ID.


```
  PUT /api/vendors/<int:id>/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `id`           | `integer`| **Required**. Unique identifier of the vendor. |

| Body Parameter | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `name`         | `string` | **Optional**. Updated name of the vendor.  |
| `contact_details`| `string`| **Optional**. Updated contact information of the vendor. |
| `address`      | `string` | **Optional**. Updated physical address of the vendor. |
| `vendor_code`  | `string` | **Optional**. Updated unique identifier for the vendor. |
| `on_time_delivery_rate`| `float`| **Optional**. Updated percentage of on-time deliveries. |
| `quality_rating_avg`| `float`| **Optional**. Updated average rating of quality based on purchase orders. |
| `average_response_time`| `float`| **Optional**. Updated average time taken to acknowledge purchase orders. |
| `fulfillment_rate`| `float`| **Optional**. Updated percentage of purchase orders fulfilled successfully. |

Description:
Updates the details of a specific vendor identified by its ID. Requires authentication using a Bearer token obtained from the token endpoint.


```
  DELETE /api/vendors/<int:id>/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `id`           | `integer`| **Required**. Unique identifier of the vendor. |

Description:
Deletes a specific vendor identified by its ID. Requires authentication using a Bearer token obtained from the token endpoint.



```
  GET /api/purchase_orders/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |

Description:
Retrieves a list of purchase orders.


```
  POST /api/purchase_orders/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |

| Body Parameter    | Type     | Description                                    |
| :---------------- | :------- | :--------------------------------------------- |
| `po_number`       | `string` | **Required**. Unique number identifying the purchase order. |
| `vendor`          | `integer`| **Required**. ID of the vendor associated with the purchase order. |
| `order_date`      | `string` | **Required**. Date when the order was placed (in ISO 8601 format). |
| `delivery_date`   | `string` | **Required**. Expected or actual delivery date of the order (in ISO 8601 format). |
| `items`           | `array`  | **Required**. Details of items ordered (JSON array of objects). |
| `quantity`        | `integer`| **Required**. Total quantity of items in the purchase order. |
| `status`          | `string` | **Required**. Current status of the purchase order (e.g., "pending", "completed", "canceled"). |
| `quality_rating`  | `float`  | **Optional**. Rating given to the vendor for this purchase order. |
| `issue_date`      | `string` | **Required**. Timestamp when the purchase order was issued to the vendor (in ISO 8601 format). |
| `acknowledgment_date` | `string` | **Optional**. Timestamp when the vendor acknowledged the purchase order (in ISO 8601 format). |

Description:
Creates a new purchase order. Requires authentication using a Bearer token obtained from the token endpoint.

```
  GET /api/purchase_orders/<int:id>/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `id`           | `integer`| **Required**. Unique identifier of the purchase order. |

Description:
Retrieves details of a specific purchase order identified by its ID.


```
  PUT /api/purchase_orders/<int:id>/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `id`           | `integer`| **Required**. Unique identifier of the purchase order. |

| Body Parameter    | Type     | Description                                    |
| :---------------- | :------- | :--------------------------------------------- |
| `po_number`       | `string` | **Optional**. Updated unique number identifying the purchase order. |
| `vendor`          | `integer`| **Optional**. Updated ID of the vendor associated with the purchase order. |
| `order_date`      | `string` | **Optional**. Updated date when the order was placed (in ISO 8601 format). |
| `delivery_date`   | `string` | **Optional**. Updated expected or actual delivery date of the order (in ISO 8601 format). |
| `items`           | `array`  | **Optional**. Updated details of items ordered (JSON array of objects). |
| `quantity`        | `integer`| **Optional**. Updated total quantity of items in the purchase order. |
| `status`          | `string` | **Optional**. Updated current status of the purchase order (e.g., "pending", "completed", "canceled"). |
| `quality_rating`  | `float`  | **Optional**. Updated rating given to the vendor for this purchase order. |
| `issue_date`      | `string` | **Optional**. Updated timestamp when the purchase order was issued to the vendor (in ISO 8601 format). |
| `acknowledgment_date` | `string` | **Optional**. Updated timestamp when the vendor acknowledged the purchase order (in ISO 8601 format). |

Description:
Updates the details of a specific purchase order identified by its ID. Requires authentication using a Bearer token obtained from the token endpoint.


```
  DELETE /api/purchase_orders/<int:id>/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `id`           | `integer`| **Required**. Unique identifier of the purchase order. |

Description:
Deletes a specific purchase order identified by its ID. Requires authentication using a Bearer token obtained from the token endpoint.

```
  GET /api/vendors/<int:vendor_id>/performance/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `vendor_id`    | `integer`| **Required**. Unique identifier of the vendor. |

Description:
Retrieves the calculated performance metrics for a specific vendor identified by its ID.

---

Explanation:
- This endpoint retrieves the performance metrics for a specific vendor, including metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.
- It requires authentication using a Bearer token obtained from the token endpoint.
- You need to provide the `vendor_id` parameter in the URL to specify the vendor for which you want to retrieve the performance metrics.


```
  POST /api/purchase_orders/<int:po_id>/acknowledge/
```

| Parameter      | Type     | Description                                |
| :------------- | :------- | :----------------------------------------- |
| `Authorization`| `string` | **Required**. Bearer token obtained from the token endpoint. |
| `po_id`        | `integer`| **Required**. Unique identifier of the purchase order. |

Description:
Acknowledges a specific purchase order identified by its ID. This endpoint updates the acknowledgment date of the purchase order and triggers the recalculation of the average response time.

---

Explanation:
- This endpoint is used by vendors to acknowledge a purchase order, which updates the acknowledgment date of the purchase order.
- It requires authentication using a Bearer token obtained from the token endpoint.
- You need to provide the `po_id` parameter in the URL to specify the purchase order that you want to acknowledge.
## Installation

Sure, here are the steps for installation:

1. **Clone the Repository:**
   ```
   git clone [https://github.com/ketanmore2002/vendor-management-system/](https://github.com/ketanmore2002/vendor-management-system/)
   ```

2. **Navigate to the Project Directory:**
   ```
   cd vendor_system
   ```

3. **Create a Virtual Environment (Optional, but Recommended):**
   ```
   python3 -m venv myenv
   ```

4. **Activate the Virtual Environment:**
   - For Windows:
     ```
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source myenv/bin/activate
     ```

5. **Install Dependencies:**
   ```
   pip3 install -r requirements.txt
   ```

6. **Apply Migrations:**
   ```
   python3 manage.py migrate
   ```

7. **Create Superuser (Optional):**
   ```
   python3 manage.py createsuperuser
   ```

8. **Run the Development Server:**
   ```
   python3 manage.py runserver
   ```

9. **Access the Application:**
   Open your web browser and go to `http://localhost:8000/` to access the application.

10. **Access the Admin Panel (Optional):**
    - Go to `http://localhost:8000/admin/` in your web browser.
    - Log in with the superuser credentials created in step 7.
