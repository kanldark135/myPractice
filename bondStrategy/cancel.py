"""
--A) 해지(일一임 해지, 부분 출금)해야 되는 사람의 매도 가격 어떻게 받아올지
1. dndn 자체 가격 -> 고객 채권 보유 내역 API 조회를 통해 파악 가능 -> !가격 어디로 input? Telegram?
2. 자문사 통해서 -> 고객이 어떤 채권을 들고 있는지에 대한 정보를 보내줘야 함

--B) 해지(모든 채권 매도하면 됨) + 부분 출금(얼마 출금 원하는지에 대한 정보 어디서 select?) => !Forrest
1. plus 해지, 부분 출금하는 동안에는 매수하는 query에 잡히면 안됨
2. 부분 출금일 경우 매수 언제부터 다시 시작? API를 통해 조회해야 하는지, query로 알 수 있는지? => !Forrest

--C) 만기일 짧은 채권부터 매도(!Ryuji께 확실히 여쭤보기)
1. 만기일이 짧을수록 매도 잘 안 된다고 하는데 어떻게 할지 => !Kwan

--D) 운영 purpose => 몇시까지 해지요청 하면 당일 매도 시작되는지(9시? 10시?) => !JB, Ryuji
1. scheduling과 연관

--E) 부분해지, 출금 signal -> 채권 가격 데이터 받기 -> 매도 수량 계산 -> 매도 API(might take more than 3 days) -> 목표금액만큼 마련되었는지 check -> 마련되었으면 다시 매수 로직(부분 해지일 경우)?
"""
