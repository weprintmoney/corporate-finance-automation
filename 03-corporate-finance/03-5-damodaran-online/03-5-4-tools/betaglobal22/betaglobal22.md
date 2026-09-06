---
title: "Betaglobal22"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal22.xls
---

# Betaglobal22

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal22.xls

Sheets: Explanation & FAQs, Industry Averages, Input Choices

## Explanation & FAQs

| End Game | To estimate pure play betas by business, to use in estimating a bottom up beta for a project or a company. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Beta | Simple average across firms of each firm's  beta, taken as a weighted average of 2-year and 5-year weekly return regression betas, with 2-year betas weighted 2/3rds. If the company has only a 2-year beta, it is used. |
| D/E Ratio | Total debt, including lease debt/ Market Value of equity. I aggregate each number across the firms and then compute the aggregate debt to equity ratio. |
| Effective Tax Rate | Effective tax rate in the most recxent 12 months. |
| Unlevered Beta | Beta/ (1+ (1-tax rate) (D/E)). You can use either a marginal or effective tax rate as your option.  |
| Cash/Firm Value | Cash & Marketable Securities/ (Market Value of Equity + Total Debt, including lease debt. Aggregated across companies first ans then computed. |
| Unlevered Beta corrected for cash | Unlevered Beta/ (1- Cash/Firm Vaue). Cash has a beta of zero. With this calculation, I remove its effect to get a pure play beta. |
| HiLo Risk | Simple average of (High Price for year - Low Price/ (High Price + Low Price). It is a non-parametric and simple measure of price risk. |
| Standard deviation (equity) | Simple average across firms of each firm's standard deviation in stock prices in the prior 2 years, using weekly returns. |
| Standard deviation (operating income) | Simple average across firms of each firm's coefficient of variation in annual operating income over prior 10 years. (Coefficient of variation is standard deviation divided by average operating income over the period) |

## Industry Averages

| Date updated: | 44931.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | if you are looking for a pure-play beta, i.e., a beta for a  business, the unlevered beta corrected for cash is your best bet. Since even sector betas can move over time, I have also reported the average of the this sector beta across time in the last column. This number, for obvious reasons, is less likely to be volatile over time. |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 362 | 1.1743473424289956 | 0.43289399542628587 |
| Aerospace/Defense | 278 | 1.0573692747052328 | 0.38676516987379195 |
| Air Transport | 155 | 0.7616142271729274 | 0.3264776350320894 |
| Apparel | 1146 | 0.8419360205243345 | 0.36521925608529593 |
| Auto & Truck | 154 | 1.033835592637108 | 0.4343868780141905 |
| Auto Parts | 746 | 1.2875467841381958 | 0.33005617851029734 |
| Bank (Money Center) | 596 | 0.4376114721606776 | 0.23431772612275084 |
| Banks (Regional) | 800 | 0.3577565862282306 | 0.18070867842041288 |
| Beverage (Alcoholic) | 220 | 0.810718193165097 | 0.29705625475632036 |
| Beverage (Soft) | 100 | 0.7947183264713243 | 0.4035093024041419 |
| Broadcasting | 135 | 0.7444295667373665 | 0.3710090994473476 |
| Brokerage & Investment Banking | 592 | 0.4509503326169772 | 0.36889500437836986 |
| Building Materials | 454 | 0.9975517318295956 | 0.32808663804141985 |
| Business & Consumer Services | 961 | 0.9967488441793113 | 0.38221100036956196 |
| Cable TV | 54 | 0.6054329946472208 | 0.33376491168446265 |
| Chemical (Basic) | 879 | 0.9877865839791308 | 0.3404058068165154 |
| Chemical (Diversified) | 68 | 0.9419506953199124 | 0.2464576111331997 |
| Chemical (Specialty) | 922 | 1.0212013193407876 | 0.3576947397473422 |
| Coal & Related Energy | 212 | 1.3528350871710502 | 0.4816592094866767 |
| Computer Services | 1105 | 1.0374271307252976 | 0.35715290547034784 |
| Computers/Peripherals | 333 | 1.2200041411476166 | 0.3545611382309401 |
| Construction Supplies | 790 | 0.9372739963088855 | 0.3322058298976089 |
| Diversified | 314 | 0.7347087450687306 | 0.31288662420834684 |
| Drugs (Biotechnology) | 1267 | 1.2526532845890637 | 0.5632862969515499 |
| Drugs (Pharmaceutical) | 1352 | 0.995463542798184 | 0.46716692912715696 |
| Education | 251 | 0.7917217099759216 | 0.39612774648641985 |
| Electrical Equipment | 1045 | 1.102323689949516 | 0.38726373019236693 |
| Electronics (Consumer & Office) | 134 | 1.0955088212486108 | 0.39500286560191095 |
| Electronics (General) | 1457 | 1.2905124151341338 | 0.36160435904068144 |
| Engineering/Construction | 1269 | 0.7301374520654016 | 0.35039244400634695 |
| Entertainment | 752 | 1.101640081025748 | 0.4608806251245198 |
| Environmental & Waste Services | 370 | 0.89640526150774 | 0.4035014250939548 |
| Farming/Agriculture | 426 | 0.659688782675045 | 0.37933135060562206 |
| Financial Svcs. (Non-bank & Insurance) | 1089 | 0.15539901285715607 | 0.3565315219729359 |
| Food Processing | 1397 | 0.6918080464880533 | 0.3329647449279708 |
| Food Wholesalers | 169 | 0.4847061410486548 | 0.3326841843873748 |
| Furn/Home Furnishings | 362 | 1.0884231491124254 | 0.3522607669321419 |
| Green & Renewable Energy | 248 | 0.7390903503257963 | 0.3831685284266511 |
| Healthcare Products | 896 | 1.0775359783236322 | 0.4707134380076722 |
| Healthcare Support Services | 460 | 0.920550044362433 | 0.4271733619949006 |
| Heathcare Information and Technology | 447 | 1.2736117177372563 | 0.4916822906703612 |
| Homebuilding | 171 | 0.9748955450608979 | 0.3301512358879997 |
| Hospitals/Healthcare Facilities | 231 | 0.5707105333941709 | 0.3595903612995441 |
| Hotel/Gaming | 650 | 0.7452374087131339 | 0.35867671029700754 |
| Household Products | 589 | 0.959250721543237 | 0.4349820087100671 |
| Information Services | 242 | 1.341638572668401 | 0.42563736147975345 |
| Insurance (General) | 206 | 0.6092906981965142 | 0.2681367395906554 |
| Insurance (Life) | 142 | 0.7962762006298993 | 0.28478714944052114 |
| Insurance (Prop/Cas.) | 235 | 0.690694218235931 | 0.3006223316059028 |
| Investments & Asset Management | 1660 | 0.565197064061528 | 0.2576393382919001 |
| Machinery | 1463 | 1.0629501446657796 | 0.3291847731521568 |
| Metals & Mining | 1783 | 1.109674282355319 | 0.507181647249953 |
| Office Equipment & Services | 144 | 0.8344943817237243 | 0.346895245167503 |
| Oil/Gas (Integrated) | 36 | 1.0257376245751695 | 0.3042421744289674 |
| Oil/Gas (Production and Exploration) | 616 | 1.1719532510287904 | 0.4962974961635102 |
| Oil/Gas Distribution | 166 | 0.640895646239336 | 0.36809312559013424 |
| Oilfield Svcs/Equip. | 455 | 0.9186144133116347 | 0.3974411197574169 |
| Packaging & Container | 414 | 0.6454232908587869 | 0.32699064372206454 |
| Paper/Forest Products | 268 | 0.752359681166661 | 0.3369474597484038 |
| Power | 485 | 0.4433046474349577 | 0.2856247136744554 |
| Precious Metals | 930 | 1.1011319908908235 | 0.541696289425715 |
| Publishing & Newspapers | 327 | 0.8690395285125317 | 0.32842913638060095 |
| R.E.I.T. | 792 | 0.5091699845154034 | 0.240091655371124 |
| Real Estate (Development) | 869 | 0.5012546023244221 | 0.3619611548510302 |
| Real Estate (General/Diversified) | 342 | 0.5297027575571283 | 0.2984152357169883 |
| Real Estate (Operations & Services) | 730 | 0.5521553535566948 | 0.3355877444396856 |
| Recreation | 323 | 0.9858976233637634 | 0.38184151451634857 |
| Reinsurance | 34 | 1.0895323174584777 | 0.28047407740457253 |
| Restaurant/Dining | 382 | 0.8289252878100836 | 0.3289600266836643 |
| Retail (Automotive) | 193 | 0.7185689332312892 | 0.3358210730125741 |
| Retail (Building Supply) | 98 | 0.9343776592100076 | 0.3164520287028011 |
| Retail (Distributors) | 1006 | 0.5976015996949612 | 0.35861499914215517 |
| Retail (General) | 189 | 0.7347606574412107 | 0.2929466934297418 |
| Retail (Grocery and Food) | 181 | 0.5285453639501723 | 0.282868950937087 |
| Retail (Online) | 342 | 1.490503406647991 | 0.5274266660321 |
| Retail (Special Lines) | 495 | 0.9561788887224327 | 0.3587125295559064 |
| Rubber& Tires | 89 | 0.9300642456688291 | 0.3021654865404598 |
| Semiconductor | 624 | 1.6715997850986177 | 0.3934866796365214 |
| Semiconductor Equip | 342 | 1.9829052012920763 | 0.3662822766481051 |
| Shipbuilding & Marine | 349 | 1.0486074968125012 | 0.3333217606223549 |
| Shoe | 85 | 0.979181546711328 | 0.36803811401947795 |
| Software (Entertainment) | 320 | 1.4648921606853302 | 0.5234856492896769 |
| Software (Internet) | 152 | 1.2628480564068731 | 0.4679621951652259 |
| Software (System & Application) | 1648 | 1.3178605209622307 | 0.48660354665715355 |
| Steel | 710 | 1.0387463631868152 | 0.3652153906745763 |
| Telecom (Wireless) | 99 | 0.5994486949624184 | 0.31576774759295073 |
| Telecom. Equipment | 461 | 1.1754366702843682 | 0.3873191497985477 |
| Telecom. Services | 295 | 0.5328634384133827 | 0.34657576559228437 |
| Tobacco | 56 | 0.7752611377217213 | 0.35147373637497514 |
| Transportation | 302 | 0.8308679841758 | 0.33819180698080703 |
| Transportation (Railroads) | 50 | 0.5377120552489277 | 0.1797251971002914 |
| Trucking | 220 | 0.8010306050790537 | 0.3311068636345737 |
| Utility (General) | 51 | 0.4455522909876226 | 0.20466102089566593 |
| Utility (Water) | 104 | 0.48577767777887526 | 0.29173364493574433 |
| Total Market | 47913 | 0.8186211841318198 | 0.3774489653276879 |
| Total Market (without financials) | 42593 | 0.9471107323884489 | 0.38973164147046063 |

## Input Choices

| Effective |
|---|
| Marginal |
