from fastapi import APIRouter, HTTPException
from models import DonationModel
from database import (
    get_all_donations, get_donation_by_id, create_donation, update_donation, delete_donation
)

donation_router = APIRouter()

@donation_router.get("/api/donations")
async def get_donations():
    return await get_all_donations()

@donation_router.get("/api/donations/{id}", response_model=DonationModel)
async def get_donation(id: str):
    donation = await get_donation_by_id(id)
    if not donation:
        raise HTTPException(status_code=404, detail=f"Donation with id {id} not found")
    return donation

@donation_router.post("/api/donations", response_model=DonationModel)
async def save_donation(donation: DonationModel):
    response = await create_donation(donation.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating donation")
    return response

@donation_router.put("/api/donations/{id}", response_model=DonationModel)
async def put_donation(id: str, donation: DonationModel):
    response = await update_donation(id, donation)
    if not response:
        raise HTTPException(status_code=404, detail=f"Donation with id {id} not found")
    return response

@donation_router.delete("/api/donations/{id}")
async def remove_donation(id: str):
    response = await delete_donation(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Donation with id {id} not found")
    return {"message": "Donation deleted successfully"}