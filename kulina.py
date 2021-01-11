kulina_df['Age'] = kulina_df['DateofBirth'].apply(lambda x : 'Adult' if  pd.Timestamp("now").year-x.year >19 and pd.Timestamp("now").year-x.year <59 
                                                      else ('Senior Adult' if pd.Timestamp("now").year-x.year >60 
                                                        else ('Teen' if  pd.Timestamp("now").year-x.year >13 and pd.Timestamp("now").year-x.year <18 else null))) 
