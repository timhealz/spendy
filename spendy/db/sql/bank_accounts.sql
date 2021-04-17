INSERT INTO spendy.bank_accounts(id, bank, owner, type, description, ledger_account)
VALUES
	('ally_th_checking', 'Ally', 'Tim', 'Checking', '', 'Assets:Tim:Cash:Ally Checking'),
    ('ally_cambridge_checking', 'Ally', 'Tim', 'Checking', '', 'Assets:Tim:Cash:Cambridge Checking'),
    ('ally_ah_checking', 'Ally', 'Aubrey', 'Checking', '', 'Assets:Aubrey:Cash:Ally Checking'),
    ('ally_healy_checking', 'Ally', 'Healy', 'Checking', '', 'Assets:Healy:Cash:Ally Checking'),
	('ally_th_savings', 'Ally', 'Tim', 'Savings', '', 'Assets:Tim:Cash:Ally Savings'),
    ('ally_ah_savings', 'Ally', 'Aubrey', 'Savings', '', 'Assets:Aubrey:Cash:Ally Savings'),
    ('ally_healy_savings', 'Ally', 'Healy', 'Savings', '', 'Assets:Healy:Cash:Ally Savings'),
    ('mecu_th_savings', 'MECU', 'Tim', 'Savings', '', 'Assets:Tim:Cash:MECU Savings'),
    ('chase_th_sapphire', 'Chase', 'Tim', 'Credit Card', 'Sapphire', 'Liabilities:Tim:Credit Cards:Chase Sapphire'),
    ('chase_th_freedom', 'Chase', 'Tim', 'Credit Card', 'Freedom', 'Liabilities:Tim:Credit Cards:Chase Freedom'),
    ('chase_ah_sapphire', 'Chase', 'Aubrey', 'Credit Card', 'Sapphire', 'Liabilities:Aubrey:Credit Cards:Chase Sapphire'),
    ('amex_healy_blue_cash', 'American Express', 'Healy', 'Credit Card', 'Blue Cash Preferred', 'Liabilities:Healy:Credit Cards:AMEX Blue Cash'),
    ('citi_healy_costco', 'Citi', 'Healy', 'Credit Card', 'Costco', 'Liabilities:Healy:Credit Cards:Citi Costco'),
    ('citi_healy_best_buy', 'Citi', 'Healy', 'Credit Card', 'Best Buy', 'Liabilities:Healy:Credit Cards:Citi Best Buy'),
    ('wells_fargo_th_rewards', 'Wells Fargo', 'Tim', 'Credit Card', 'Rewards', 'Liabilities:Tim:Credit Cards:Wells Fargo Rewards'),
    ('target_healy_redcard', 'Target', 'Healy', 'Credit Card', 'Redcard', 'Liabilities:Healy:Credit Cards:Target Redcard')
;
