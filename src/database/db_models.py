"""DB Models"""

from sqlalchemy import Column, Integer, String

from src.database.db import Base


class NetworkDevice(Base):
    __tablename__ = "network_devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ne_name = Column(String(100), unique=True, nullable=False, index=True)
    lte_ip = Column(String(100), nullable=True)
    gsm_ip = Column(String(100), nullable=True)
    gnodeb_ip = Column(String(100), nullable=True)
    loop_ip = Column(String(100), nullable=True)
    ike_peer = Column(String(100), nullable=True)
    enodeb_id = Column(Integer, nullable=True)
    gnodeb_id = Column(Integer, nullable=True)