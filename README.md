# DigitalOcean Functions: Send Email using AWS SES
This function will send templated (by Jinja) email message with image attachment using AWS SES to the specified email address. 
May be useful for landing (marketing) static website which contains "Contact Us" form.

## Configuration
Copy `env.example` to `.env` and adjust environment variables values

## Deploy
```
doctl serverless deploy .
```

## Use
```
curl -X POST <FUNCTION_URL> \
   -H "Content-Type: application/json" \
   -d '{"your_name": "Denis"}'
```

## Epilog
- As endpoint can be called from any source it worth to add recaptcha integration to avoid bots spam you for your money
- Endpoint can be called without params using "Trigger", for example every 4 minutes to keep function warm to avoid cold-starts (5 sec)