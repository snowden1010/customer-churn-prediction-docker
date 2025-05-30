# API Documentation

## Endpoints

### POST /predict
- **Description:** Predict customer churn for a given input.
- **Request Body:** JSON with customer features.
- **Response:** JSON with prediction result (churn: true/false, probability, etc.)

### GET /health
- **Description:** Health check endpoint.
- **Response:** JSON with status message.

---

## Example Request

```
POST /predict
Content-Type: application/json
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```

## Example Response
```
{
  "churn": true,
  "probability": 0.87
}
```
