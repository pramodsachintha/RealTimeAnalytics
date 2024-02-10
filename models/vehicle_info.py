from dataclasses import dataclass


@dataclass
class VehicleInfo:
    car_id: int
    session_time: float
    lap_time: float
    lap_distance: float
    total_distance: float
    x_position: float
    y_position: float
    z_position: float
    speed: float
    throttle: float
    brake: float
    clutch: float
    gear: int
    steer: float
    normalized_steer: float
    engine_rpm: int
    drs: int
    engine_temperature: int
    fuel_remaining: float
    fuel_capacity: float
    in_pits: int
    sector: int
    lap_invalid: int
    penalties: int
    ai_controlled: int
    pit_limiter_on: int
    front_left_wing_damage: int
    front_right_wing_damage: int
    rear_wing_damage: int
    engine_damage: int
    gear_box_damage: int
    vehicle_fia_flags: int
