SECONDS=0


bash scripts/case-generator.sh   
echo "executed case-generator.sh"

bash scripts/complete-vaccination-generator.sh  
echo "executed complete-vaccination-generator.sh"

bash scripts/edge-generator.sh                  
echo "executed edge-generator.sh"

bash scripts/peaks-generator.sh
echo "executed peaks-generator.sh"

bash scripts/vaccinated-count-generator.sh
echo "executed vaccinated-count-generator.sh"

bash scripts/vaccinated-ratio-generator.sh 
echo "executed vaccinated-ratio-generator.sh"

bash scripts/vaccination-population-ratio-generator.sh
echo "executed vaccination-population-ratio-generator.sh"

bash scripts/vaccine-type-ratio-generator.sh
echo "executed vaccine-type-ratio-generator.sh"

echo "Finished. Please check the 'output' directory for the resultant CSV files."

echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
