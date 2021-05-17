@app.route('/water_levels', methods=['GET'])
def handle_water_levels():
    if request.method == 'GET':
        water_levels = WaterLevelModel.query.all()
        results = [
            {
                "name": water.name,
                "height": water.height
            } for water in water_levels]

        return {"count": len(results), "water_level": results}
