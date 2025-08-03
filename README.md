# Visa Recommendation CLI Tool

A simple command-line tool that recommends travel destinations based on visa accessibility using the [Henley Passport Index](https://www.henleyglobal.com/passport-index) API.

## ✈️ What It Does

This CLI tool allows you to input your country of passport and outputs a categorized list of countries you can travel to based on visa requirements:

- Visa Free
- Visa on Arrival
- eVisa
- Visa Required

## Key Features: 

Key Features:

- No API keys required
- Real-time visa status data
- Clean CLI interface with categorized output
- Works with just Python and requests

---

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/visa-recommender-cli.git
cd visa-recommender-cli
```

### 2. Run the CLI

python visa_recommender.py       
Enter your country of passport: india

Note : Case-insensitive — both India and india work.

### 3. Expected Output: 

Fetching destinations for passport: India...
Visa Free (59 countries):
Bhutan, Indonesia, Jamaica, Kenya, Nepal, Qatar, Serbia, Thailand, ...

Visa on Arrival (23 countries):
Cambodia, Laos, Maldives, Sri Lanka, ...

eVisa (16 countries):
Australia, Turkey, etc.

Visa Required (120 countries):
USA, UK, Canada, China, Germany, etc.

### Actual Output: 
<img width="1772" height="187" alt="image" src="https://github.com/user-attachments/assets/4fe0db3e-a031-4257-8742-888958d743df" />
<img width="1765" height="192" alt="image" src="https://github.com/user-attachments/assets/8b7ed062-7e85-4d35-9bd3-1b38194504e2" />



### 4. How it Works: 

- Pulls live data from the Henley Passport Index API
- Categorizes destinations based on visa type
- Case-insensitive country matching
- Prints grouped recommendations directly in your terminal

### 5. Future Improvements: 

- Add optional export to CSV/Markdown
- Integrate RESTCountries API to enrich output with flags and region info
- Filter by region (Asia, Europe, etc.)
- Add caching to avoid repeated API calls
- Build as installable CLI tool (pip install visa-cli)

### 6. Contributing: 
Pull requests are welcome!      
For major changes, open an issue first to discuss what you would like to change.
 
