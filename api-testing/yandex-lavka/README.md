# Yandex Lavka — API Testing

**Project type:** individual training project  
**Scope:** REST and XML API testing  
**Focus:** request validation, response contracts, CRUD operations, negative scenarios, and requirements gaps

## Tools

- Postman
- Swagger / API documentation
- cURL
- JSON and XML
- Chrome DevTools / Network
- SQL for related data checks

## Coverage

- positive and negative requests;
- required and optional fields;
- missing `id` and `quantity` parameters;
- valid and invalid data types;
- empty, null, and malformed values;
- boundary values;
- unsupported values and logically impossible combinations;
- status codes and complete response bodies;
- GET, POST, PUT, and DELETE flows;
- preparation and cleanup of test data;
- comparison of expected and actual API behaviour.

## Example validation matrix

| Scenario | Expected behaviour |
|---|---|
| Valid request body | Success status and documented response body |
| Required field omitted | `400 Bad Request` with validation details |
| Wrong data type | `400 Bad Request` |
| Logically invalid value | `400 Bad Request` |
| Non-existent resource ID | Documented not-found response |
| Malformed JSON/XML | `400 Bad Request` |
| Boundary value | Accepted or rejected according to the exact requirement |

## Test documentation principles

- Expected and actual results include both the status code and full relevant response body.
- Preconditions contain only requests needed to prepare test data.
- Syntax errors are separated from logical validation errors.
- A test is not marked passed merely because the request can be sent.
- Requirements gaps are documented before inventing expected behaviour.

## Representative grey areas

- behaviour when both dependent fields are missing;
- precedence when several validation rules fail at once;
- whether zero and negative values are syntactically valid but logically forbidden;
- exact error schema and message stability;
- idempotency and repeated deletion;
- cleanup of dependent data.

## What this demonstrates

- contract-based API testing;
- careful distinction between transport, syntax, validation, and business logic;
- reproducible preparation of test data;
- verification of response bodies rather than status codes alone;
- ability to challenge incomplete requirements.