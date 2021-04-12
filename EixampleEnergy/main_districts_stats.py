from EixampleEnergy.tool import load_shapefile


def clean_data(df):
    # df = df[df['House_cons'] < 20000]
    df = df[df['House_cons'] > 0]
    df = df[df['BARRI'].notnull()]
    return df


def main():
    df = load_shapefile('../data/BCN_Private_communities_barrios/BCN_Private_communities_4326_SJ_barrios.shp')
    df = clean_data(df)
    barrio_ids = df[['BARRI']].squeeze().unique()
    barrio_ids.sort()
    for barrio_id in barrio_ids:
        print("\nBARRI id: ", barrio_id)
        df_barrio = df[df['BARRI'] == barrio_id]

        nb_buildings = len(df_barrio.index)
        print("Number of buildings: ", nb_buildings)

        sum_build_consumption = df_barrio['Build_cons'].sum()
        print("Total Energy Consumption: ", round(sum_build_consumption))

        sum_build_co2 = df_barrio['Build_CO2'].sum()
        print("Total CO2 emission: ", round(sum_build_co2))

        avg_build_date = df_barrio['build_date'].apply(lambda bdate: float(bdate)).mean()
        print("Average building age: ", round(avg_build_date))

        sum_build_surface = df_barrio['build_surf'].sum()
        sum_build_surface = sum_build_surface * ureg['meter**2']
        # print("Total building surface: ", round(sum_build_surface))
        print(f'Total building surface:  {sum_build_surface:~H}')


if __name__ == '__main__':
    main()
