from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, TIMESTAMP

HungTHP1Base = declarative_base()

class Token(HungTHP1Base):
    __tablename__ = 'hungth1token'  
    hungth1_token_id = Column(Integer, primary_key=True)
    hungthp1_owner_id = Column(Integer, nullable=False)  
    hungth1_token = Column(String(15), nullable=False)
    hungth1_created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    hungthp1_used_at = Column(TIMESTAMP)
    def __repr__(self):  
          return (f"<Token(hungth1_token_id={self.hungth1_token_id}, "
                f"hungthp1_owner_id={self.hungthp1_owner_id}, "
                f"hungth1_token='{self.hungth1_token}', "
                f"hungth1_created_at='{self.hungth1_created_at}', "
                f"hungthp1_used_at='{self.hungthp1_used_at}')>")