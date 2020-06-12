export interface GensetData {
    Id : string,
    name : string,
    detail : string,
    tank_capacity : number,
    displacement : string,
    starting_system : string,
    design_features : string,
    full_load_consumption : number,
    three_quarter_load_consumption : number,
    half_load_consumption : number,
    quarter_load_consumption : number,
    bore_stroke : string,
    continuous_rated_output : number,
    voltage_allowance: string
}

export interface GensetSavedData {
    genset_ASI_genset_name: string,
    genset_ASI_genset_voltage_allowance : string,
    genset_ASI_genset_details : string,
    genset_ASI_genset_starting_system : string,
    genset_ASI_genset_design_features : string,
    genset_ASI_genset_tank_capacity : number,
    genset_ASI_genset_displacement : string,
    genset_ASI_genset_full_load_consumption : number,
    genset_ASI_genset_three_quarter_load_consumption : number,
    genset_ASI_genset_half_load_consumption : number,
    genset_ASI_genset_quarter_load_consumption : number,
    genset_ASI_genset_bore_stroke : string,
    genset_ASI_genset_continuous_rated_output : number
}

export interface AvgTempData{
    temp: number,
    engine_off: number
}

export interface loginData{
    username: string,
    user_type: string,
    password: string,
    users_secret: string,
    access: string

}

export class UsersType {
  constructor(public typeCode:string, public typeName:string) {
  }
}
