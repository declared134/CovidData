

-- use projectportfolio

-- total death rate among US cases

-- select location, date, total_cases, total_deaths, 
-- 	 (total_deaths/total_cases)*100 as death_rate
-- from CovidDeaths
-- where location like '%state%' and total_cases is not NULL
-- order by 1, 2

-- countries with highest infection rate compared to population
-- select location, date, 
--     max(total_cases) as HighestInfections,
--     max(total_cases/population) as InfectionRate
-- from CovidDeaths
-- group by location, date
-- order by InfectionRate desc

-- countries with highest death count by population
-- select location, DATE, max(total_deaths) as DeathCount, 
--     max(total_deaths/population) as DeathRate
-- from coviddeaths
-- where continent is not null
-- group by location, date
-- order by DeathCount desc

-- global new cases and new deaths
-- Select SUM(new_cases) as total_cases, 
-- SUM(new_deaths ) as total_deaths, 
-- SUM(new_deaths)/SUM(New_Cases)*100 as DeathPercentage
-- From CovidDeaths
-- where continent is not null 
-- order by 1,2

-- select location, date,  total_vaccinations/population as VaccRate
-- from coviddeaths
-- where total_vaccinations is not null
-- order by VaccRate desc

-- global new cases and new deaths
-- Select SUM(new_cases) as total_cases, 
-- SUM(new_deaths ) as total_deaths, 
-- SUM(new_deaths)/SUM(New_Cases)*100 as DeathPercentage
-- From CovidDeaths
-- where continent is not null 
-- order by 1,2



-- select dea.continent,
-- dea.location,
-- dea.date,
-- dea.population,
-- vac.new_vaccinations,
-- sum(vac.new_vaccinations) OVER
-- -- sum of vacs by location
-- (partition by dea.location
-- order by dea.location, dea.date) as RoliingPeopleVaccinated
-- from coviddeaths dea
-- join covidvaccinations vac
-- 	on dea.location = vac.location
--     and dea.date = vac.date
-- where dea.continent is not null
-- order by 2,3

-- use CTE

-- with PopVsVac (continent, location,
-- date, population, new_vaccinaions, 
-- RollingPeopleVaccinated)
-- as
-- (
-- select dea.continent,
-- dea.location,
-- dea.date,
-- dea.population,
-- vac.new_vaccinations,
-- sum(vac.new_vaccinations) OVER
-- (partition by dea.location
-- order by dea.location, dea.date) as RoliingPeopleVaccinated
-- from coviddeaths dea
-- join covidvaccinations vac
-- 	on dea.location = vac.location
--     and dea.date = vac.date
-- where dea.continent is not null

-- )

-- Select *, (RollingPeopleVaccinated/Population)*100 as RollPercentage
-- From PopVsVac

-- temp table

-- drop temporary table PercentPopulationVaccinated
-- Create temporary Table PercentPopulationVaccinated
-- (
-- Continent nvarchar(255),
-- Location nvarchar(255),
-- Date datetime,
-- Population numeric,
-- New_vaccinations numeric,
-- RollingPeopleVaccinated numeric
-- )

-- insert into PercentPopulationVaccinated
-- select dea.continent,
-- dea.location,
-- dea.date,
-- dea.population,
-- vac.new_vaccinations,
-- sum(vac.new_vaccinations) OVER
-- -- sum of vacs by location
-- (partition by dea.location
-- order by dea.location, dea.date) as RoliingPeopleVaccinated
-- from coviddeaths dea
-- join covidvaccinations vac
-- 	on dea.location = vac.location
--     and dea.date = vac.date
-- where dea.continent is not null
-- order by 2,3

-- Select *, (RollingPeopleVaccinated/Population)*100 as RollPercentage
-- From PercentPopulationVaccinated

-- creating view to store data for later visulaizations

create view  PercentPopulationVaccinated aspercentpopulationvaccinated
select dea.continent,
dea.location,
dea.date,
dea.population,
vac.new_vaccinations,
sum(vac.new_vaccinations) OVER
-- sum of vacs by location
(partition by dea.location
order by dea.location, dea.date) as RoliingPeopleVaccinated
from coviddeaths dea
join covidvaccinations vac
	on dea.location = vac.location
    and dea.date = vac.date
where dea.continent is not null
order by 2,3

select *
from PercentPopulationVaccinated





