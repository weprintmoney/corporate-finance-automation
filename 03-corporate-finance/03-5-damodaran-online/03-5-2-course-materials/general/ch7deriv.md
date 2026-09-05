---
title: "Chapter 7 derivations"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/AppldCF/derivn/ch7deriv.html
---

Chapter 7 derivations

### *Discussion Issues and Derivations*

1. *A Simple Test of Debt*To check where on the spectrum between straight debt and straight equity these securities fall, answer the following questions:  
   1. Are the payments on the securities contractual or residual?  
   - If contractual, it is closer to debt  
   - If residual, it is closer to equity  
   2. Are the payments tax deductible?  
   - If yes, it is closer to debt  
   - If no, if is closer to equity  
   3. Do the cash flows on the security have a high priority or a low priority if the firm is in financial trouble?  
   - If it has high priority, it is closer to debt.  
   - If it has low priority, it is closer to equity.  
   4. Does the security have a fixed life?  
   - If yes, it is closer to debt  
   - If no, it is closer to equity  
   5. Does the owner of the security get a share of the control of management of the firm?  
   - If no, it is closer to debt.  
   - If yes, if is closer to equity  
   - *The Treatment of Hybrid Securities*Hybrid securities represent a combination of debt and equity. The cleanest way of dealing with hybrid securities is to break them up into debt and equity components. For instance, the value of a convertible debt can be decomposed into straight debt and equity components. Since the price of a convertible bond is the sum of the straight debt and the call option components, the value of the straight bond component in conjunction with the market price should be sufficient to estimate the call option component, which is also the equity component:  
     Value of Equity Component = Price of Convertible Bond - Value of Straight Bond Component  
     The value of the straight bond component can be estimated using the coupon payments on the convertible bond, the maturity of the bond and the market interest rate the company would have to pay on a straight debt issue. This last input can be estimated directly if the company also trades straight bonds in the market place, or it can be based upon the bond rating, if any, assigned to the company.  
     For instance, assume that you have a 10-year convertible bond, with a 5% coupon rate trading at $ 1,050, and that the company has a debt rating of BBB (with a market interest rate of 8%). The value of the straight bond and equity components can be estimated as follows:  
     Straight Bond Component = $ 50 (PVA, 10 years,8%) + 1000/1.0810 = $798.69  
     Equity Component = $ 1,050 - $ 799 = $ 251  
     The straight bond component is added to other debt in the cost of capital formulation and assigned the regular cost of debt, and the equity component is added on to equity and assigned the cost of equity.- *The Treatment of Warrants and Convertibles*Warrants and conversion options (in convertible bonds, for instance) are long term call options, but standard option pricing models are based upon the assumption that exercising an option does not affect the value of the underlying asset. This may be true for listed options on stocks, but it is not true for warrants and convertibles, since their exercise increases the number of shares outstanding and brings in fresh cash into the firm, both of which will affect the stock price. The expected negative impact (dilution) of exercise will make warrants less valuable than otherwise similar call options. The adjustment for dilution in the Black-Scholes to the stock price involves three steps:  
       Step 1: The stock price is adjusted for the expected dilution from warrant exercise.  
       Dilution-adjusted S = (S ns+W nw) / ns   
       where,  
       S = Current value of the stock nw = Number of warrants outstanding   
       W = Market value of warrants outstanding ns = Number of shares outstanding  
       When the warrants are exercised, the number of shares outstanding will increase, reducing the stock price. The numerator reflects the market value of equity, including both stocks and warrants outstanding.  
       Step 2: The variance used in the option pricing formula is the variance in the value of the equity in the company (i.e., the value of stocks plus warrants, not just the stocks).  
       Step 3: The call is valued with these inputs.  
       Dilution-adjusted value = Call Value from model   
       - *Valuing Flexibility*When making financial decisions, managers consider the effects such decisions will have on their capacity to take new projects or meet unanticipated contingencies in future periods. Practically, this translates into firms maintaining excess debt capacity or larger cash balances than are warranted by current needs, to meet unexpected future requirements. While maintaining this financing flexibility has value to firms, it also has a cost; the large cash balances earn low returns and excess debt capacity implies that the firm is giving up some value and has a higher cost of capital.   
         The value of flexibility can be analyzed using the option pricing framework; a firm maintains large cash balances and excess debt capacity in order to have the option to take projects that might arise in the future. The value of this option will depend upon two key variables:  
         1. Quality of the Firm’s Projects: It is the excess return that the firm earns on its projects that provides the value to flexibility. Other things remaining equal, firms operating in businesses where projects earn substantially higher returns than their hurdle rates should value flexibility more than those that operate in stable businesses where excess returns are small.  
         2. Uncertainty about Future Projects: If flexibility is viewed as an option, its value will increase when there is greater uncertainty about future projects; thus, firms with predictable capital expenditures should value flexibility less than those with high variability in capital expenditures.  
         This option framework would imply that firms such as Microsoft and Compaq, which earn large excess returns on their projects and face more uncertainty about future investment needs, can justify holding large cash balances and excess debt capacity, whereas a firm such as Chrysler, with much smaller excess returns and more predictable investment needs, should hold a much smaller cash balance and less excess debt. In fact, the value of flexibility can be calculated as a percentage of firm value, with the following inputs for the option pricing model.  
         S = Annual Net Capital Expenditures as percent of Firm Value (1 + Excess Return)  
         K = Annual Net Capital Expenditures as percent of Firm Value  
         t = 1 year  
         s2 = Variance in ln(Net Capital Expenditures)  
         y = Annual Cost of Holding Cash or Maintaining Excess Debt Capacity as % of Firm Value  
         To illustrate, assume that a firm which earns 18% on its projects has a cost of capital of 13%, and that net capital expenditures are 10% of firm value; the variance in ln(net capital expenditures) is 0.04. Also assume that the firm could have a cost of capital of 12% if it used its excess debt capacity. The value of flexibility as a percentage of firm value can be estimated as follows:  
         S = 10% (1.05) = 10.50% [Excess Return = 18% - 13% = 5%]  
         K = 10%  
         t = 1 year  
         s2 = 0.04  
         y = 13% - 12% = 1%  
         Based on these inputs and a riskless rate of 5%, the value of flexibility is 1.31% of firm value.  
         - *Dilution as a Bogey*The dilution effect refers to the possible decrease in earnings per share from any action that might lead to an increase in the number of shares outstanding. As evidenced in surveys, managers, especially in the United States, weigh these potential dilution effects heavily in decisions on what type of financing to use, and how to fund projects. Consider, for instance, the choice between raising equity using a rights issue, where the stock is issued at a price below the current market price, and a public issue of stock at the market price. The latter is a much more expensive option, from the perspective of investment banking fees and other costs, but is chosen, nevertheless, because it results in fewer shares being issued (to raise the same amount of funds). The fear of dilution is misplaced for the following reasons:  
           1. Investors measure their returns in terms of total return and not just in terms of stock price. While the stock price will go down more after a rights issue, each investor will be compensated adequately for the price drop (by either receiving more shares or by being able to sell their rights to other investors). In fact, if the transactions costs are considered, stockholders will be better off after a rights issue than after an equivalent public issue of stock.  
           2. While the earnings per share will always drop in the immediate aftermath of a new stock issue, the stock price will not necessarily follow suit. In particular, if the stock issue is used to finance a good project (i.e., a project with a positive net present value), the increase in value should be greater than the increase in the number of shares, leading to a higher stock price.  
           Ultimately, the measure of whether a company should issue stock to finance a project should depend upon the quality of the investment. Firms that dilute their stockholdings to take good investments are choosing the right course for their stockholders.
