{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Initial imports\n",
    "import os\n",
    "import pandas as pd\n",
    "import requests\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_general_recent_crypto_news():\n",
    "    \n",
    "    load_dotenv()\n",
    "    api_key = os.getenv(\"crypto_news_key\")\n",
    "    general_crypto_news_data = 'https://cryptonews-api.com/api/v1/category?section=general&items=50&token='+ api_key\n",
    "    response_news = requests.get(general_crypto_news_data)\n",
    "    news_data_raw = response_news.json()\n",
    "    news_df = pd.DataFrame(data=news_data_raw['data'])\n",
    "    general_recent_news_df = news_df.drop(columns = ['news_url','image_url','source_name'])\n",
    "    \n",
    "    return general_recent_news_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>date</th>\n",
       "      <th>topics</th>\n",
       "      <th>sentiment</th>\n",
       "      <th>type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Altcoins spike to new highs while Bitcoin bull...</td>\n",
       "      <td>Terra (LUNA), Basic Attention Token and Cardan...</td>\n",
       "      <td>Tue, 16 Mar 2021 18:05:00 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Visa CEO talks bitcoin, stablecoin service str...</td>\n",
       "      <td>Visa CEO Al Kelly dug into the credit card com...</td>\n",
       "      <td>Tue, 16 Mar 2021 16:41:52 -0400</td>\n",
       "      <td>[stablecoins]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Visa CEO Claims Cryptocurrencies Could Become ...</td>\n",
       "      <td>Visa CEO Al Kelly wants his company to be in t...</td>\n",
       "      <td>Tue, 16 Mar 2021 15:18:00 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Domino Effect: Is India The Start Of Weaker Go...</td>\n",
       "      <td>This week, it was revealed that India would se...</td>\n",
       "      <td>Tue, 16 Mar 2021 11:30:16 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Signal Accepts Cryptocurrency Donations, App G...</td>\n",
       "      <td>On March 16, 2021, Signal tweeted: ???As a nonpr...</td>\n",
       "      <td>Tue, 16 Mar 2021 06:56:00 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>New Details About India Banning Cryptocurrency...</td>\n",
       "      <td>New details have emerged suggesting that the I...</td>\n",
       "      <td>Tue, 16 Mar 2021 06:30:39 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Investview reveals it holds over $1M in Bitcoi...</td>\n",
       "      <td>Investview, a popular U.S-based financial serv...</td>\n",
       "      <td>Tue, 16 Mar 2021 02:00:45 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Bitcoin Breaks Key Support, Ethereum and Altco...</td>\n",
       "      <td>Bitcoin price extended its decline below the U...</td>\n",
       "      <td>Tue, 16 Mar 2021 01:53:13 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Warnings as Crypto, Digital Yuan Fraudsters Ru...</td>\n",
       "      <td>Chinese media outlets are reporting a sharp ri...</td>\n",
       "      <td>Mon, 15 Mar 2021 22:00:00 -0400</td>\n",
       "      <td>[digital yuan]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Turkish Government Warms Up to Crypto, Charts ...</td>\n",
       "      <td>A senior Turkish government minister says he l...</td>\n",
       "      <td>Mon, 15 Mar 2021 17:39:41 -0400</td>\n",
       "      <td>[regulations]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>6,000+ XRP Holders Want to Testify, Bitcoin St...</td>\n",
       "      <td>Get your daily, bite-sized digest of cryptoass...</td>\n",
       "      <td>Mon, 15 Mar 2021 13:37:00 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>There's a New Challenge in the Crypto Area</td>\n",
       "      <td>If you are a big fan of Bitcoin trading, then ...</td>\n",
       "      <td>Mon, 15 Mar 2021 13:30:00 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Several Binance Smart Chain Projects Under DNS...</td>\n",
       "      <td>A DNS attack can take several forms. However, ...</td>\n",
       "      <td>Mon, 15 Mar 2021 12:11:31 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Vast Majority of Accredited Investors Plan To ...</td>\n",
       "      <td>The bulk of accredited investors are consideri...</td>\n",
       "      <td>Mon, 15 Mar 2021 12:10:47 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Financial Services Company Discloses $1 Millio...</td>\n",
       "      <td>Another public company now has a six-figure su...</td>\n",
       "      <td>Mon, 15 Mar 2021 12:05:05 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Nasdaq-Listed Mining Company Riot Blockchain R...</td>\n",
       "      <td>Riot Blockchain mined $10 million worth of Bit...</td>\n",
       "      <td>Mon, 15 Mar 2021 10:31:31 -0400</td>\n",
       "      <td>[mining]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Reserve Bank of Australia Looks to Tap Blockch...</td>\n",
       "      <td>The Reserve Bank of Australia is actively exam...</td>\n",
       "      <td>Mon, 15 Mar 2021 10:25:37 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Over $2.24 Billion Liquidated as Crypto Market...</td>\n",
       "      <td>The bears have a stronghold on the market afte...</td>\n",
       "      <td>Mon, 15 Mar 2021 09:25:43 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Over $2 Billion in Futures Liquidated as Crypt...</td>\n",
       "      <td>The prices of Bitcoin and other major cryptocu...</td>\n",
       "      <td>Mon, 15 Mar 2021 08:56:47 -0400</td>\n",
       "      <td>[futures]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>South Korean crypto exchange volumes surpass t...</td>\n",
       "      <td>The country is one of the biggest markets for ...</td>\n",
       "      <td>Mon, 15 Mar 2021 08:49:19 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Korean Crypto Trading Volume Has Surpassed The...</td>\n",
       "      <td>Crypto traders in South Korea have pushed cryp...</td>\n",
       "      <td>Mon, 15 Mar 2021 08:40:27 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Here Are the Top 10 Research Tools for Crypto ...</td>\n",
       "      <td>The pseudonymous Coin Bureau host is outlining...</td>\n",
       "      <td>Mon, 15 Mar 2021 07:45:02 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>India's Proposed Crypto Ban Leaves Future Unce...</td>\n",
       "      <td>Plans to restrict the use of cryptocurrency in...</td>\n",
       "      <td>Mon, 15 Mar 2021 07:09:44 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>India To Introduce All Out Cryptocurrency Ban ...</td>\n",
       "      <td>India is reportedly gearing up to introduce a ...</td>\n",
       "      <td>Mon, 15 Mar 2021 05:05:10 -0400</td>\n",
       "      <td>[mining]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Latest Episode of India's Crypto Ban Soap Draw...</td>\n",
       "      <td>Yet another ???unnamed Indian government source???...</td>\n",
       "      <td>Mon, 15 Mar 2021 04:23:55 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>New reports of India's crypto ban re-emerge af...</td>\n",
       "      <td>The Indian government is reportedly planning t...</td>\n",
       "      <td>Mon, 15 Mar 2021 03:40:17 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Crypto Strategist Says Two Altcoins Are Heavil...</td>\n",
       "      <td>Popular crypto analyst and trader Micha??l van ...</td>\n",
       "      <td>Mon, 15 Mar 2021 03:04:06 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>India: Rough waters ahead as officials confide...</td>\n",
       "      <td>Every time Bitcoin???s price rallies, traders ge...</td>\n",
       "      <td>Mon, 15 Mar 2021 02:45:16 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Bitcoin, Ethereum and Altcoins Correct Gains</td>\n",
       "      <td>Bitcoin price rallied above the USD 60,000 res...</td>\n",
       "      <td>Mon, 15 Mar 2021 02:00:22 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Alameda Research invests $2M into crypto marke...</td>\n",
       "      <td>Alameda Research has invested $2 million in a ...</td>\n",
       "      <td>Mon, 15 Mar 2021 00:50:12 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Supply chain tokens see triple-digit gains as ...</td>\n",
       "      <td>Supply chain projects like OriginTrail, Walton...</td>\n",
       "      <td>Sun, 14 Mar 2021 20:14:59 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Reported volume of top South Korean crypto exc...</td>\n",
       "      <td>The increase in volume came as the price of Bi...</td>\n",
       "      <td>Sun, 14 Mar 2021 16:43:03 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Lawmakers Introduce Bill To Bring Long-Awaited...</td>\n",
       "      <td>Lawmakers have proposed new legislation to cla...</td>\n",
       "      <td>Sun, 14 Mar 2021 15:00:46 -0400</td>\n",
       "      <td>[regulations]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>A $5.7 Million Crypto Heist Leaves Social Toke...</td>\n",
       "      <td>It appears to have been due to a compromised R...</td>\n",
       "      <td>Sun, 14 Mar 2021 14:35:54 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>Social token platform Roll suffers exploit, to...</td>\n",
       "      <td>Roll, a platform for issuing social tokens on ...</td>\n",
       "      <td>Sun, 14 Mar 2021 13:37:03 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>The superheated NFTs? A crypto market niche ti...</td>\n",
       "      <td>A pyramid scheme where ???somebody will be burnt...</td>\n",
       "      <td>Sun, 14 Mar 2021 10:07:00 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>9 Crypto Assets Have Massive Potential in Marc...</td>\n",
       "      <td>Altcoin Daily host and crypto analyst Austin A...</td>\n",
       "      <td>Sun, 14 Mar 2021 04:04:11 -0400</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>Turkish authorities arrest 18 Chinese national...</td>\n",
       "      <td>While the cryptocurrency market was witnessing...</td>\n",
       "      <td>Sat, 13 Mar 2021 08:45:19 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>Spanish Ministry of Economy Proposes to Create...</td>\n",
       "      <td>Crypto regulation in Spain remains on the poli...</td>\n",
       "      <td>Fri, 12 Mar 2021 19:30:29 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>Two Crypto Assets Could See Imminent Exponenti...</td>\n",
       "      <td>Popular crypto analyst Josh Rager is naming tw...</td>\n",
       "      <td>Fri, 12 Mar 2021 17:45:37 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Altcoins sell-off after Bitcoin price rejects ...</td>\n",
       "      <td>Altcoins are witnessing a bout of profit-takin...</td>\n",
       "      <td>Fri, 12 Mar 2021 17:30:00 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Negative</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>China May Target Tether after Digital Yuan Lau...</td>\n",
       "      <td>Tether (USDT) could emerge as an unlikely targ...</td>\n",
       "      <td>Fri, 12 Mar 2021 14:00:00 -0500</td>\n",
       "      <td>[stablecoins, digital yuan]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>MicroStrategy Does Its Bitcoin Thing Again, Ma...</td>\n",
       "      <td>Get your daily, bite-sized digest of cryptoass...</td>\n",
       "      <td>Fri, 12 Mar 2021 11:51:16 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>CFTC investigating Binance for American crypto...</td>\n",
       "      <td>Binance began kicking U.S. customers off its p...</td>\n",
       "      <td>Fri, 12 Mar 2021 11:42:45 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>U.S. Regulator CFTC Investigates Binance</td>\n",
       "      <td>As reported by Bloomberg, the United States Co...</td>\n",
       "      <td>Fri, 12 Mar 2021 11:05:20 -0500</td>\n",
       "      <td>[regulations]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>???Beeple' NFT sold for $69 million is the fourt...</td>\n",
       "      <td>Is money even real anymore? The NFT sector is ...</td>\n",
       "      <td>Fri, 12 Mar 2021 10:39:40 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>Biden's Stimulus Check to Push Crypto Market t...</td>\n",
       "      <td>On March 6, the House of Representatives appro...</td>\n",
       "      <td>Fri, 12 Mar 2021 10:32:50 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>Markets Report: Bitcoin aims for top 3 weekly ...</td>\n",
       "      <td>The past week's trading has been one big guess...</td>\n",
       "      <td>Fri, 12 Mar 2021 09:42:59 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>Poltergeist exchange partners with ghost by Mc...</td>\n",
       "      <td>Poltergeist Exchange has partnered with GHOST ...</td>\n",
       "      <td>Fri, 12 Mar 2021 09:00:23 -0500</td>\n",
       "      <td>[stablecoins]</td>\n",
       "      <td>Positive</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Binance reportedly under CFTC investigation ov...</td>\n",
       "      <td>The world's largest cryptocurrency exchange is...</td>\n",
       "      <td>Fri, 12 Mar 2021 09:00:10 -0500</td>\n",
       "      <td>[]</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>Article</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                title  \\\n",
       "0   Altcoins spike to new highs while Bitcoin bull...   \n",
       "1   Visa CEO talks bitcoin, stablecoin service str...   \n",
       "2   Visa CEO Claims Cryptocurrencies Could Become ...   \n",
       "3   Domino Effect: Is India The Start Of Weaker Go...   \n",
       "4   Signal Accepts Cryptocurrency Donations, App G...   \n",
       "5   New Details About India Banning Cryptocurrency...   \n",
       "6   Investview reveals it holds over $1M in Bitcoi...   \n",
       "7   Bitcoin Breaks Key Support, Ethereum and Altco...   \n",
       "8   Warnings as Crypto, Digital Yuan Fraudsters Ru...   \n",
       "9   Turkish Government Warms Up to Crypto, Charts ...   \n",
       "10  6,000+ XRP Holders Want to Testify, Bitcoin St...   \n",
       "11         There's a New Challenge in the Crypto Area   \n",
       "12  Several Binance Smart Chain Projects Under DNS...   \n",
       "13  Vast Majority of Accredited Investors Plan To ...   \n",
       "14  Financial Services Company Discloses $1 Millio...   \n",
       "15  Nasdaq-Listed Mining Company Riot Blockchain R...   \n",
       "16  Reserve Bank of Australia Looks to Tap Blockch...   \n",
       "17  Over $2.24 Billion Liquidated as Crypto Market...   \n",
       "18  Over $2 Billion in Futures Liquidated as Crypt...   \n",
       "19  South Korean crypto exchange volumes surpass t...   \n",
       "20  Korean Crypto Trading Volume Has Surpassed The...   \n",
       "21  Here Are the Top 10 Research Tools for Crypto ...   \n",
       "22  India's Proposed Crypto Ban Leaves Future Unce...   \n",
       "23  India To Introduce All Out Cryptocurrency Ban ...   \n",
       "24  Latest Episode of India's Crypto Ban Soap Draw...   \n",
       "25  New reports of India's crypto ban re-emerge af...   \n",
       "26  Crypto Strategist Says Two Altcoins Are Heavil...   \n",
       "27  India: Rough waters ahead as officials confide...   \n",
       "28       Bitcoin, Ethereum and Altcoins Correct Gains   \n",
       "29  Alameda Research invests $2M into crypto marke...   \n",
       "30  Supply chain tokens see triple-digit gains as ...   \n",
       "31  Reported volume of top South Korean crypto exc...   \n",
       "32  Lawmakers Introduce Bill To Bring Long-Awaited...   \n",
       "33  A $5.7 Million Crypto Heist Leaves Social Toke...   \n",
       "34  Social token platform Roll suffers exploit, to...   \n",
       "35  The superheated NFTs? A crypto market niche ti...   \n",
       "36  9 Crypto Assets Have Massive Potential in Marc...   \n",
       "37  Turkish authorities arrest 18 Chinese national...   \n",
       "38  Spanish Ministry of Economy Proposes to Create...   \n",
       "39  Two Crypto Assets Could See Imminent Exponenti...   \n",
       "40  Altcoins sell-off after Bitcoin price rejects ...   \n",
       "41  China May Target Tether after Digital Yuan Lau...   \n",
       "42  MicroStrategy Does Its Bitcoin Thing Again, Ma...   \n",
       "43  CFTC investigating Binance for American crypto...   \n",
       "44           U.S. Regulator CFTC Investigates Binance   \n",
       "45  ???Beeple' NFT sold for $69 million is the fourt...   \n",
       "46  Biden's Stimulus Check to Push Crypto Market t...   \n",
       "47  Markets Report: Bitcoin aims for top 3 weekly ...   \n",
       "48  Poltergeist exchange partners with ghost by Mc...   \n",
       "49  Binance reportedly under CFTC investigation ov...   \n",
       "\n",
       "                                                 text  \\\n",
       "0   Terra (LUNA), Basic Attention Token and Cardan...   \n",
       "1   Visa CEO Al Kelly dug into the credit card com...   \n",
       "2   Visa CEO Al Kelly wants his company to be in t...   \n",
       "3   This week, it was revealed that India would se...   \n",
       "4   On March 16, 2021, Signal tweeted: ???As a nonpr...   \n",
       "5   New details have emerged suggesting that the I...   \n",
       "6   Investview, a popular U.S-based financial serv...   \n",
       "7   Bitcoin price extended its decline below the U...   \n",
       "8   Chinese media outlets are reporting a sharp ri...   \n",
       "9   A senior Turkish government minister says he l...   \n",
       "10  Get your daily, bite-sized digest of cryptoass...   \n",
       "11  If you are a big fan of Bitcoin trading, then ...   \n",
       "12  A DNS attack can take several forms. However, ...   \n",
       "13  The bulk of accredited investors are consideri...   \n",
       "14  Another public company now has a six-figure su...   \n",
       "15  Riot Blockchain mined $10 million worth of Bit...   \n",
       "16  The Reserve Bank of Australia is actively exam...   \n",
       "17  The bears have a stronghold on the market afte...   \n",
       "18  The prices of Bitcoin and other major cryptocu...   \n",
       "19  The country is one of the biggest markets for ...   \n",
       "20  Crypto traders in South Korea have pushed cryp...   \n",
       "21  The pseudonymous Coin Bureau host is outlining...   \n",
       "22  Plans to restrict the use of cryptocurrency in...   \n",
       "23  India is reportedly gearing up to introduce a ...   \n",
       "24  Yet another ???unnamed Indian government source???...   \n",
       "25  The Indian government is reportedly planning t...   \n",
       "26  Popular crypto analyst and trader Micha??l van ...   \n",
       "27  Every time Bitcoin???s price rallies, traders ge...   \n",
       "28  Bitcoin price rallied above the USD 60,000 res...   \n",
       "29  Alameda Research has invested $2 million in a ...   \n",
       "30  Supply chain projects like OriginTrail, Walton...   \n",
       "31  The increase in volume came as the price of Bi...   \n",
       "32  Lawmakers have proposed new legislation to cla...   \n",
       "33  It appears to have been due to a compromised R...   \n",
       "34  Roll, a platform for issuing social tokens on ...   \n",
       "35  A pyramid scheme where ???somebody will be burnt...   \n",
       "36  Altcoin Daily host and crypto analyst Austin A...   \n",
       "37  While the cryptocurrency market was witnessing...   \n",
       "38  Crypto regulation in Spain remains on the poli...   \n",
       "39  Popular crypto analyst Josh Rager is naming tw...   \n",
       "40  Altcoins are witnessing a bout of profit-takin...   \n",
       "41  Tether (USDT) could emerge as an unlikely targ...   \n",
       "42  Get your daily, bite-sized digest of cryptoass...   \n",
       "43  Binance began kicking U.S. customers off its p...   \n",
       "44  As reported by Bloomberg, the United States Co...   \n",
       "45  Is money even real anymore? The NFT sector is ...   \n",
       "46  On March 6, the House of Representatives appro...   \n",
       "47  The past week's trading has been one big guess...   \n",
       "48  Poltergeist Exchange has partnered with GHOST ...   \n",
       "49  The world's largest cryptocurrency exchange is...   \n",
       "\n",
       "                               date                       topics sentiment  \\\n",
       "0   Tue, 16 Mar 2021 18:05:00 -0400                           []  Positive   \n",
       "1   Tue, 16 Mar 2021 16:41:52 -0400                [stablecoins]  Positive   \n",
       "2   Tue, 16 Mar 2021 15:18:00 -0400                           []  Positive   \n",
       "3   Tue, 16 Mar 2021 11:30:16 -0400                           []  Negative   \n",
       "4   Tue, 16 Mar 2021 06:56:00 -0400                           []   Neutral   \n",
       "5   Tue, 16 Mar 2021 06:30:39 -0400                           []   Neutral   \n",
       "6   Tue, 16 Mar 2021 02:00:45 -0400                           []   Neutral   \n",
       "7   Tue, 16 Mar 2021 01:53:13 -0400                           []   Neutral   \n",
       "8   Mon, 15 Mar 2021 22:00:00 -0400               [digital yuan]  Negative   \n",
       "9   Mon, 15 Mar 2021 17:39:41 -0400                [regulations]  Negative   \n",
       "10  Mon, 15 Mar 2021 13:37:00 -0400                           []   Neutral   \n",
       "11  Mon, 15 Mar 2021 13:30:00 -0400                           []  Negative   \n",
       "12  Mon, 15 Mar 2021 12:11:31 -0400                           []  Negative   \n",
       "13  Mon, 15 Mar 2021 12:10:47 -0400                           []  Positive   \n",
       "14  Mon, 15 Mar 2021 12:05:05 -0400                           []  Positive   \n",
       "15  Mon, 15 Mar 2021 10:31:31 -0400                     [mining]   Neutral   \n",
       "16  Mon, 15 Mar 2021 10:25:37 -0400                           []  Positive   \n",
       "17  Mon, 15 Mar 2021 09:25:43 -0400                           []  Negative   \n",
       "18  Mon, 15 Mar 2021 08:56:47 -0400                    [futures]  Negative   \n",
       "19  Mon, 15 Mar 2021 08:49:19 -0400                           []  Positive   \n",
       "20  Mon, 15 Mar 2021 08:40:27 -0400                           []  Positive   \n",
       "21  Mon, 15 Mar 2021 07:45:02 -0400                           []  Positive   \n",
       "22  Mon, 15 Mar 2021 07:09:44 -0400                           []  Negative   \n",
       "23  Mon, 15 Mar 2021 05:05:10 -0400                     [mining]   Neutral   \n",
       "24  Mon, 15 Mar 2021 04:23:55 -0400                           []   Neutral   \n",
       "25  Mon, 15 Mar 2021 03:40:17 -0400                           []   Neutral   \n",
       "26  Mon, 15 Mar 2021 03:04:06 -0400                           []  Positive   \n",
       "27  Mon, 15 Mar 2021 02:45:16 -0400                           []   Neutral   \n",
       "28  Mon, 15 Mar 2021 02:00:22 -0400                           []  Positive   \n",
       "29  Mon, 15 Mar 2021 00:50:12 -0400                           []  Positive   \n",
       "30  Sun, 14 Mar 2021 20:14:59 -0400                           []  Positive   \n",
       "31  Sun, 14 Mar 2021 16:43:03 -0400                           []  Positive   \n",
       "32  Sun, 14 Mar 2021 15:00:46 -0400                [regulations]   Neutral   \n",
       "33  Sun, 14 Mar 2021 14:35:54 -0400                           []  Negative   \n",
       "34  Sun, 14 Mar 2021 13:37:03 -0400                           []  Negative   \n",
       "35  Sun, 14 Mar 2021 10:07:00 -0400                           []   Neutral   \n",
       "36  Sun, 14 Mar 2021 04:04:11 -0400                           []  Positive   \n",
       "37  Sat, 13 Mar 2021 08:45:19 -0500                           []  Negative   \n",
       "38  Fri, 12 Mar 2021 19:30:29 -0500                           []   Neutral   \n",
       "39  Fri, 12 Mar 2021 17:45:37 -0500                           []  Positive   \n",
       "40  Fri, 12 Mar 2021 17:30:00 -0500                           []  Negative   \n",
       "41  Fri, 12 Mar 2021 14:00:00 -0500  [stablecoins, digital yuan]   Neutral   \n",
       "42  Fri, 12 Mar 2021 11:51:16 -0500                           []   Neutral   \n",
       "43  Fri, 12 Mar 2021 11:42:45 -0500                           []   Neutral   \n",
       "44  Fri, 12 Mar 2021 11:05:20 -0500                [regulations]   Neutral   \n",
       "45  Fri, 12 Mar 2021 10:39:40 -0500                           []   Neutral   \n",
       "46  Fri, 12 Mar 2021 10:32:50 -0500                           []  Positive   \n",
       "47  Fri, 12 Mar 2021 09:42:59 -0500                           []   Neutral   \n",
       "48  Fri, 12 Mar 2021 09:00:23 -0500                [stablecoins]  Positive   \n",
       "49  Fri, 12 Mar 2021 09:00:10 -0500                           []   Neutral   \n",
       "\n",
       "       type  \n",
       "0   Article  \n",
       "1   Article  \n",
       "2   Article  \n",
       "3   Article  \n",
       "4   Article  \n",
       "5   Article  \n",
       "6   Article  \n",
       "7   Article  \n",
       "8   Article  \n",
       "9   Article  \n",
       "10  Article  \n",
       "11  Article  \n",
       "12  Article  \n",
       "13  Article  \n",
       "14  Article  \n",
       "15  Article  \n",
       "16  Article  \n",
       "17  Article  \n",
       "18  Article  \n",
       "19  Article  \n",
       "20  Article  \n",
       "21  Article  \n",
       "22  Article  \n",
       "23  Article  \n",
       "24  Article  \n",
       "25  Article  \n",
       "26  Article  \n",
       "27  Article  \n",
       "28  Article  \n",
       "29  Article  \n",
       "30  Article  \n",
       "31  Article  \n",
       "32  Article  \n",
       "33  Article  \n",
       "34  Article  \n",
       "35  Article  \n",
       "36  Article  \n",
       "37  Article  \n",
       "38  Article  \n",
       "39  Article  \n",
       "40  Article  \n",
       "41  Article  \n",
       "42  Article  \n",
       "43  Article  \n",
       "44  Article  \n",
       "45  Article  \n",
       "46  Article  \n",
       "47  Article  \n",
       "48  Article  \n",
       "49  Article  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "get_general_recent_crypto_news()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:pyvizenv] *",
   "language": "python",
   "name": "conda-env-pyvizenv-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
